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
Nuage VSD Sim utils
"""

import ConfigParser
import logging
import sys
import uuid

from vspk import v5_0 as vsdk
from flask_restful import abort

NUAGE_API_DATA = {
    'ROOT_UUIDS': {
        'csproot_user': '',
        'csp_enterprise': ''
    },
    'USERS': {},
    'ENTERPRISES': {},
    'ENTERPRISE_USERS': {},
    'USER_ENTERPRISE': {}
}

def parse_config(config_file):
    """
    Parses configuration file
    """
    cfg = ConfigParser.ConfigParser()
    cfg.read(config_file)

    # Checking the LOG options
    if not cfg.has_option('LOG', 'directory') or \
            not cfg.has_option('LOG', 'file') or \
            not cfg.has_option('LOG', 'level'):
        print 'Missing options in the LOG section of configuration file {0:s}, please check the sample configuration'.format(
            config_file)
        sys.exit(1)

    return cfg


def configure_logging(level, path):
    """
    Configures the logging environment
    """
    logging.basicConfig(filename=path, format='%(asctime)s %(levelname)s %(message)s', level=level)
    logger = logging.getLogger(__name__)

    return logger

def find_entities_by_field(data, field, value):
    """
    Find and return an aray of entities based on a field and value in a dict
    Returns a dict (empty if no matching entities were found
    """
    result = []
    if data and field and value and len(data) > 0 and hasattr(data.itervalues().next(), field):
        result = list(v for k, v in data.iteritems() if getattr(v, field) == value)
    return result

def abort_check(data, field, value):
    if len(find_entities_by_field(data=data, field=field, value=value)) == 0:
        abort(404, message='Unable to find entity with field {0} and value {1}'.format(field, value))

def init_base_entities():
    """
    Sets up basic entities for use
    """
    global NUAGE_API_DATA

    csproot = vsdk.NUUser(
        id=str(uuid.uuid1()),
        user_name='csproot',
        password='csproot',
        first_name='csproot',
        last_name='csproot',
        email = 'csproot@CSP.com',
        parent_type='ENTERPRISE'
    )
    csp = vsdk.NUEnterprise(
        id=str(uuid.uuid1()),
        name='CSP',
        description='Enterprise that contains all the CSP users',
        allowed_forwarding_classes=['E', 'F', 'G', 'H'],
        allow_gateway_management=True,
        allow_advanced_qos_configuration=True,
        allow_trusted_forwarding_class=True,
        bgp_enabled=True,
        creation_date=1383734246000,
        customer_id=10002,
        dictionary_version=2,
        enable_application_performance_management=False,
        entity_scope='ENTERPRISE',
        floating_ips_quota=0,
        floating_ips_used=0,
        ldap_authorization_enabled=False,
        ldap_enabled=False,
        last_updated_by=csproot.id,
        last_updated_date=1499101329000
    )
    csproot.parent_id = csp.id

    NUAGE_API_DATA['ENTERPRISE_USERS'][csp.id] = [csproot.id]
    NUAGE_API_DATA['USER_ENTERPRISE'][csproot.id] = [csp.id]
    NUAGE_API_DATA['ROOT_UUIDS']['csp_enterprise'] = csp.id
    NUAGE_API_DATA['ENTERPRISES'][csp.id] = csp
    NUAGE_API_DATA['ROOT_UUIDS']['csproot_user'] = csproot.id
    NUAGE_API_DATA['USERS'][csproot.id] = csproot

    logging.info('Created base entities')
    logging.debug(NUAGE_API_DATA)
