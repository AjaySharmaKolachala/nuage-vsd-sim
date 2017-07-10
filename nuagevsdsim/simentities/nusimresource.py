# BSD 3-Clause License
#
# Copyright (c) 2017, Philippe Dellaert
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
enterprise
"""
import logging
import json
import random
import time
import uuid

from vspk import v5_0 as vsdk
from flask_restful import Resource, request, abort
from nuagevsdsim.common.utils import NUAGE_API_DATA, get_idiomatic_name


class NUSimResource(Resource):

    __vspk_class__ = None
    __unique_fields__ = []
    __mandatory_fields__ = []

    def __init__(self):
        pass

    def get(self, entity_id=None):
        logging.debug('{0:s} get request received'.format(self.__vspk_class__.rest_name))

        if entity_id:
            self._abort_missing_entity('id', entity_id)
            return [NUAGE_API_DATA[self.__vspk_class__.rest_name][entity_id].to_dict()]
        elif entity_id == '':
            if self.__vspk_class__ == vsdk.NUEnterprise:
                return list(
                    i.to_dict() for k, i in NUAGE_API_DATA[self.__vspk_class__.rest_name].iteritems() if k != NUAGE_API_DATA['ROOT_UUIDS']['csp_enterprise'])
            return list(i.to_dict() for k, i in NUAGE_API_DATA[self.__vspk_class__.rest_name].iteritems())

    def delete(self, entity_id=None):
        logging.debug('{0:s} delete request received'.format(self.__vspk_class__.rest_name))

        if entity_id == NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']:
            return_data = {
                'errors': [{
                    'property': '',
                    'descriptions': [
                        {
                            'description': 'System user cannot be deleted.',
                            'title': 'System user cannot be deleted'
                        }
                    ]
                }],
                "internalErrorCode": 2013
            }
            abort(409, **return_data)

        if entity_id == NUAGE_API_DATA['ROOT_UUIDS']['csp_enterprise']:
            return_data = {
                'errors': [{
                    'property': '',
                    'descriptions': [
                        {
                            'description': 'System enterprise cannot be deleted.',
                            'title': 'System enterprise cannot be deleted'
                        }
                    ]
                }],
                "internalErrorCode": 2010
            }
            abort(409, **return_data)

        self._abort_missing_entity('id', entity_id)
        if entity_id:
            del NUAGE_API_DATA[self.__vspk_class__.rest_name][entity_id]
        return '', 204

    def put(self, entity_id=None):
        logging.debug('{0:s} put request received'.format(self.__vspk_class__.rest_name))
        logging.debug('args: {0}'.format(request.data))
        self._abort_missing_entity('id', entity_id)

        if entity_id:
            data = json.loads(request.data)

            for field in self.__mandatory_fields__:
                self._abort_mandatory_field(data=data, field=field)
            for field in self.__unique_fields__:
                self._abort_duplicate_field(data=data, field=field)

            data = self._parse_data(data)
            logging.debug('data: {0}'.format(data))
            old_entity = NUAGE_API_DATA[self.__vspk_class__.rest_name][entity_id]
            new_entity = self.__vspk_class__(**data)
            new_entity.id = old_entity.id
            if hasattr(new_entity, 'creation_date'):
                new_entity.creation_date = old_entity.creation_date
            if hasattr(new_entity, 'last_updated_by'):
                new_entity.last_updated_by=NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']
            if hasattr(new_entity, 'last_updated_date'):
                new_entity.last_updated_date=int(time.time()*1000)
            if hasattr(new_entity, 'customer_id'):
                new_entity.customer_id = old_entity.customer_id
            if hasattr(new_entity, 'dictionary_version'):
                new_entity.dictionary_version = 2

            NUAGE_API_DATA[self.__vspk_class__.rest_name][new_entity.id] = new_entity
            return [NUAGE_API_DATA[self.__vspk_class__.rest_name][new_entity.id].to_dict()], 201

    def _find_entities_by_field(self, data, field, value):
        result = []
        if data and field and value and len(data) > 0 and hasattr(data.itervalues().next(), field):
            result = list(v for k, v in data.iteritems() if getattr(v, field) == value)
        return result

    def _abort_mandatory_field(self, data=None, field=None):
        if field not in data.keys() or not data[field]:
            return_data = {
                'errors': [{
                    'property': field,
                    'descriptions': [
                        {
                            'description': 'This value cannot be null',
                            'title': 'Invalid input. Value cannot be null'
                        }
                    ]
                }],
                "internalErrorCode": 5001
            }
            abort(409, **return_data)

    def _abort_duplicate_field(self, data=None, field=None):
        if field not in data.keys() or (data[field] and len(self._find_entities_by_field(NUAGE_API_DATA[self.__vspk_class__.rest_name], field, data[field])) > 0):
            return_data = {
                'errors': [{
                    'property': field,
                    'descriptions': [
                        {
                            'description': 'Another {0:s} with the same {1:s} = {2:s} exists.'.format(self.__vspk_class__.rest_name, field, data[field]),
                            'title': 'Cannot create duplicate entity.'
                        }
                    ]
                }],
                "internalErrorCode": 9501
            }
            abort(409, **return_data)

    def _abort_missing_entity(self, field, value):
        if len(self._find_entities_by_field(data=NUAGE_API_DATA[self.__vspk_class__.rest_name], field=field, value=value)) == 0:
            abort(404, message='Unable to find entity with field {0} and value {1}'.format(field, value))

    def _parse_data(self, data=dict()):
        new_data = {}
        for key, value in data.iteritems():
            new_data[get_idiomatic_name(key)] = value
        return new_data

class NUSimResources(NUSimResource):

    __vspk_class__ = None
    __unique_fields__ = []
    __mandatory_fields__ = []
    __default_fields__ = {}

    def __init__(self):
        super(NUSimResources, self).__init__()

    def get(self, entity_id=None):
        logging.debug('{0:s} list get request received'.format(self.__vspk_class__.rest_name))
        if self.__vspk_class__ == vsdk.NUEnterprise:
            return list(
                i.to_dict() for k, i in NUAGE_API_DATA[self.__vspk_class__.rest_name].iteritems() if k != NUAGE_API_DATA['ROOT_UUIDS']['csp_enterprise'])

        return list(i.to_dict() for k, i in NUAGE_API_DATA[self.__vspk_class__.rest_name].iteritems())

    def post(self):
        logging.debug('{0:s} post request received'.format(self.__vspk_class__.rest_name))
        logging.debug('args: {0}'.format(request.data))
        data = json.loads(request.data)

        for field in self.__mandatory_fields__:
            self._abort_mandatory_field(data=data, field=field)
        for field in self.__unique_fields__:
            self._abort_duplicate_field(data=data, field=field)
        for field, value in self.__default_fields__.iteritems():
            if field not in data.keys() or not data[field]:
                data[field] = value

        data = self._parse_data(data)
        logging.debug('data: {0}'.format(data))

        entity = self.__vspk_class__(**data)
        entity.id = str(uuid.uuid1())
        if hasattr(entity, 'owner'):
            entity.owner = NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']
        if hasattr(entity, 'creation_date'):
            entity.creation_date = int(time.time()*1000)
        if hasattr(entity, 'last_updated_by'):
            entity.last_updated_by = NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']
        if hasattr(entity, 'last_updated_date'):
            entity.last_updated_date = int(time.time()*1000)
        if hasattr(entity, 'customer_id'):
            entity.customer_id = 10000+random.randint(0,89999)
        if hasattr(entity, 'dictionary_version'):
            entity.dictionary_version = 2

        NUAGE_API_DATA[self.__vspk_class__.rest_name][entity.id] = entity
        return [NUAGE_API_DATA[self.__vspk_class__.rest_name][entity.id].to_dict()], 201