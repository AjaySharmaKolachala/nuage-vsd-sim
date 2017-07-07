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

ROOT_UUIDS = {
    'csproot_user': '',
    'csp_enterprise': ''
}
USERS = {}
ENTERPRISES = {}

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

def init_base_entities():
    """
    Sets up basic entities for use
    """
    global ROOT_UUIDS, USERS, ENTERPRISES

    _csproot = vsdk.NUUser(
        id=str(uuid.uuid1()), user_name='csproot',
        first_name='csproot',
        last_name='csproot',
        email = 'csproot@CSP.com'
    )
    ROOT_UUIDS['csproot_user'] = _csproot.id
    USERS[_csproot.id] = _csproot

    _csp = vsdk.NUEnterprise(
        id=str(uuid.uuid1()),
        name='CSP',
        description='Enterprise that contains all the CSP users',
        customer_id=10002,
        creation_date=1383734246000,
        last_updated_date=1499101329000,
        last_updated_by=_csproot.id
    )
    ROOT_UUIDS['csp_enterprise'] = _csp.id
    ENTERPRISES[_csp.id] = _csp

    logging.info('Created base entities')
    logging.debug('Root UUIDs: {0}'.format(ROOT_UUIDS))
    logging.debug('Users: {0}'.format(USERS))
    logging.debug('Enterprises: {0}'.format(ENTERPRISES))
