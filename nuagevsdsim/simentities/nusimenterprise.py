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
from flask_restful import Resource, request
from nuagevsdsim.common.utils import NUAGE_API_DATA, abort_check


class NUSimEnterprise(Resource):

    def get(self, entity_id=None):
        logging.debug('enterprise get request received')
        abort_check(NUAGE_API_DATA['ENTERPRISES'], 'id', entity_id)

        if entity_id:
            return [NUAGE_API_DATA['ENTERPRISES'][entity_id].to_dict()]


    def delete(self, entity_id=None):
        logging.debug('enterperise delete request received')
        abort_check(NUAGE_API_DATA['ENTERPRISES'], 'id', entity_id)

        if entity_id:
            del NUAGE_API_DATA['ENTERPRISES'][entity_id]
            return '', 204

    def put(self, entity_id=None):
        logging.debug('enterperise put request received')
        logging.debug('args: {0}'.format(request.data))
        abort_check(NUAGE_API_DATA['ENTERPRISES'], 'id', entity_id)

        if entity_id:
            data = json.loads(request.data)
            old_entity = NUAGE_API_DATA['ENTERPRISES'][entity_id]
            new_entity = vsdk.NUEnterprise(**data)
            new_entity.id = old_entity.id
            new_entity.creation_date = old_entity.creation_date
            new_entity.last_updated_by=NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']
            new_entity.last_updated_date=int(time.time()*1000)
            new_entity.customer_id = old_entity.customer_id
            new_entity.dictionary_version = 2

            NUAGE_API_DATA['ENTERPRISES'][new_entity.id] = new_entity
            return [NUAGE_API_DATA['ENTERPRISES'][new_entity.id].to_dict()], 201


class NUSimEnterprises(Resource):

    def get(self, entity_id=None):
        logging.debug('enterprise list get request received')
        return list(i.to_dict() for k, i in NUAGE_API_DATA['ENTERPRISES'].iteritems() if k != NUAGE_API_DATA['ROOT_UUIDS']['csp_enterprise'])

    def post(self):
        logging.debug('enterprise post request received')
        logging.debug('args: {0}'.format(request.data))

        data = json.loads(request.data)
        entity = vsdk.NUEnterprise(**data)
        entity.id = str(uuid.uuid1())
        entity.owner = NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']
        entity.creation_date = int(time.time()*1000)
        entity.last_updated_by = NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']
        entity.last_updated_date = int(time.time()*1000)
        entity.customer_id = 10000+random.randint(0,89999)
        entity.dictionary_version = 2
        if not 'BGPEnabled' in data.keys() or not data['BGPEnabled']:
            entity.bgp_enabled = False
        if not 'DHCPLeaseInterval' in data.keys() or not data['DHCPLeaseInterval']:
            entity.dhcp_lease_interval = 24
        if not 'entityScope' in data.keys() or not data['entityScope']:
            entity.entity_scope = 'ENTERPRISE'
        if not 'floatingIPsQuota' in data.keys() or not data['floatingIPsQuota']:
            entity.floating_ips_quota = 24
        if not 'floatingIPsUsed' in data.keys() or not data['floatingIPsUsed']:
            entity.floating_ips_used = 0
        if not 'LDAPAuthorizationEnabled' in data.keys() or not data['LDAPAuthorizationEnabled']:
            entity.ldap_authorization_enabled = False
        if not 'LDAPEnabled' in data.keys() or not data['LDAPEnabled']:
            entity.ldap_enabled = False
        if not 'allowedForwardingClasses' in data.keys() or not data['allowedForwardingClasses']:
            entity.allowed_forwarding_classes = ['H']


        NUAGE_API_DATA['ENTERPRISES'][entity.id] = entity
        return [NUAGE_API_DATA['ENTERPRISES'][entity.id].to_dict()], 201