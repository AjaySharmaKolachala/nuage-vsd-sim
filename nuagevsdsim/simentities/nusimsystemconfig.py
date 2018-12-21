# -*- coding: utf-8 -*-
# BSD 3-Clause License
#
# Copyright (c) 2017, Nokia
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
NUSimSystemConfig
"""
from vspk import v5_0 as vsdk

from nuagevsdsim.simentities.nusimresource import NUSimResource

class NUSimSystemConfig(NUSimResource):
    """ Represents a SystemConfig

        Notes:
            The System Configuration which can be dynamically managed using REST Api.
    """

    __vspk_class__ = vsdk.NUSystemConfig
    __unique_fields__ = ['externalID']
    __mandatory_fields__ = []
    __default_fields__ = {
        'AARFlowStatsInterval': 30,
        'AARProbeStatsInterval': 30,
        'ACLAllowOrigin': '*',
        'ECMPCount': 1,
        'LDAPSyncInterval': 600,
        'LDAPTrustStoreCertifcate': '/usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts',
        'LDAPTrustStorePassword': 'changeit',
        'ADGatewayPurgeTime': 7200,
        'RDLowerLimit': 0,
        'RDPublicNetworkLowerLimit': 0,
        'RDPublicNetworkUpperLimit': 65535,
        'RDUpperLimit': 65535,
        'ZFBRequestRetryTimer': 30,
        'ZFBSchedulerStaleRequestTimeout': 1440,
        'PGIDLowerLimit': 65536,
        'PGIDUpperLimit': 2147483647,
        'DHCPOptionSize': 16,
        'VLANIDLowerLimit': 0,
        'VLANIDUpperLimit': 0,
        'VMCacheSize': 5000,
        'VMPurgeTime': 60,
        'VMResyncDeletionWaitTime': 2,
        'VMResyncOutstandingInterval': 1000,
        'VMUnreachableCleanupTime': 7200,
        'VMUnreachableTime': 3600,
        'VNFTaskTimeout': 3600,
        'VNIDLowerLimit': 1,
        'VNIDPublicNetworkLowerLimit': 1,
        'VNIDPublicNetworkUpperLimit': 16777215,
        'VNIDUpperLimit': 1048575,
        'APIKeyRenewalInterval': 300,
        'APIKeyValidity': 86400,
        'VPortInitStatefulTimer': 300,
        'LRUCacheSizePerSubnet': 32,
        'VSDReadOnlyMode': False,
        'NSGUplinkHoldDownTimer': 5,
        'ASNumber': 65534,
        'VSSStatsInterval': 30,
        'RTLowerLimit': 0,
        'RTPublicNetworkLowerLimit': 0,
        'RTPublicNetworkUpperLimit': 65535,
        'RTUpperLimit': 65535,
        'EVPNBGPCommunityTagASNumber': 65534,
        'EVPNBGPCommunityTagLowerLimit': 0,
        'EVPNBGPCommunityTagUpperLimit': 65535,
        'pageMaxSize': 500,
        'pageSize': 50,
        'maxResponse': 500,
        'accumulateLicensesEnabled': False,
        'perDomainVlanIdEnabled': False,
        'serviceIDUpperLimit': 2147483648,
        'offsetCustomerID': 10000,
        'offsetServiceID': 20001,
        'virtualFirewallRulesEnabled': False,
        'ejbcaNSGCertificateProfile': 'VSPClient',
        'ejbcaNSGEndEntityProfile': 'NSG',
        'ejbcaOCSPResponderCN': 'ocspsigner',
        'ejbcaOCSPResponderURI': 'http://localhost:7080/ejbca/publicweb/status/ocsp',
        'ejbcaVspRootCa': 'VSPCA',
        'alarmsMaxPerObject': 10,
        'elasticClusterName': 'nuage_elasticsearch',
        'allowEnterpriseAvatarOnNSG': True,
        'importedSaaSApplicationsVersion': '1.0',
        'inactiveTimeout': 600000,
        'infrastructureBGPASNumber': 65500,
        'postProcessorThreadsCount': 20,
        'nsgBootstrapEndpoint': 'https://proxy-bootstrap:12443/nuage/api',
        'nsgConfigEndpoint': 'https://{proxyDNSName}:11443/nuage/api',
        'nsgLocalUiUrl': 'http://registration.nsg',
        'esiID': 10000,
        'csprootAuthenticationMethod': 'LOCAL',
        'stackTraceEnabled': False,
        'statefulACLNonTCPTimeout': 180,
        'statefulACLTCPTimeout': 3600,
        'staticWANServicePurgeTime': 3600,
        'statsCollectorAddress': 'localhost',
        'statsCollectorPort': '29090',
        'statsCollectorProtoBufPort': '39090',
        'statsMaxDataPoints': 10000,
        'statsMinDuration': 2592000,
        'statsNumberOfDataPoints': 30,
        'statsTSDBServerAddress': 'http://localhost:9300',
        'stickyECMPIdleTimeout': 0,
        'attachProbeToIPsecNPM': True,
        'attachProbeToVXLANNPM': True,
        'subnetResyncInterval': 10,
        'subnetResyncOutstandingInterval': 20,
        'customerIDUpperLimit': 2147483647,
        'avatarBasePath': '/opt/vsd/jboss/standalone/deployments/CloudMgmt-web.war',
        'avatarBaseURL': 'https://localhost:8443',
        'eventLogCleanupInterval': 3600,
        'eventLogEntryMaxAge': 7,
        'eventProcessorInterval': 250,
        'eventProcessorMaxEventsCount': 100,
        'eventProcessorTimeout': 25000,
        'twoFactorCodeExpiry': 300,
        'twoFactorCodeLength': 6,
        'twoFactorCodeSeedLength': 96,
        'dynamicWANServiceDiffTime': 1,
        'syslogDestinationHost': 'http://localhost',
        'sysmonCleanupTaskInterval': 20,
        'sysmonNodePresenceTimeout': 3600,
        'sysmonProbeResponseTimeout': 30
    }
    __get_parents__ = ['me']
    __create_parents__ = []

    def __init__(self):
        super(NUSimSystemConfig, self).__init__()