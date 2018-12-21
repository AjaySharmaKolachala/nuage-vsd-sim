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
NUSimGlobalMetadata
"""
from vspk import v5_0 as vsdk

from nuagevsdsim.simentities.nusimresource import NUSimResource

class NUSimGlobalMetadata(NUSimResource):
    """ Represents a GlobalMetadata

        Notes:
            Metadata associated to a entity.
    """

    __vspk_class__ = vsdk.NUGlobalMetadata
    __unique_fields__ = ['externalID']
    __mandatory_fields__ = ['blob']
    __default_fields__ = {
        
    }
    __get_parents__ = ['addressmap', 'addressrange', 'alarm', 'allalarm', 'allgateway', 'allredundancygroup', 'application', 'applicationbinding', 'applicationperformancemanagement', 'applicationperformancemanagementbinding', 'autodiscoveredgateway', 'avatar', 'bfdsession', 'bgpneighbor', 'bgppeer', 'bgpprofile', 'bootstrap', 'bootstrapactivation', 'brconnection', 'bridgeinterface', 'bulkstatistics', 'certificate', 'cms', 'component', 'connectionendpoint', 'container', 'containerinterface', 'containerresync', 'cosremarkingpolicy', 'cosremarkingpolicytable', 'csnatpool', 'ctranslationmap', 'customproperty', 'defaultgateway', 'demarcationservice', 'deploymentfailure', 'destinationurl', 'dhcpoption', 'diskstat', 'domain', 'domaintemplate', 'dscpforwardingclassmapping', 'dscpforwardingclasstable', 'dscpremarkingpolicy', 'dscpremarkingpolicytable', 'ducgroup', 'ducgroupbinding', 'eamconfig', 'egressaclentrytemplate', 'egressacltemplate', 'egressadvfwdentrytemplate', 'egressadvfwdtemplate', 'egressdomainfloatingipaclentrytemplate', 'egressdomainfloatingipacltemplate', 'egressprofile', 'egressqospolicy', 'enterprise', 'enterprisenetwork', 'enterprisepermission', 'enterpriseprofile', 'enterprisesecureddata', 'enterprisesecurity', 'eventlog', 'firewallacl', 'firewallrule', 'floatingip', 'forwardingpathlist', 'forwardingpathlistentry', 'gateway', 'gatewayredundantport', 'gatewaysecureddata', 'gatewaysecurity', 'gatewayslocation', 'gatewaytemplate', 'globalmetadata', 'group', 'groupkeyencryptionprofile', 'hostinterface', 'hsc', 'ikecertificate', 'ikeencryptionprofile', 'ikegateway', 'ikegatewayconfig', 'ikegatewayconnection', 'ikegatewayprofile', 'ikepsk', 'ikesubnet', 'infraconfig', 'infrastructureaccessprofile', 'infrastructureevdfprofile', 'infrastructuregatewayprofile', 'infrastructurevscprofile', 'ingressaclentrytemplate', 'ingressacltemplate', 'ingressadvfwdentrytemplate', 'ingressadvfwdtemplate', 'ingressprofile', 'ingressqospolicy', 'ipfilterprofile', 'ipreservation', 'ipv6filterprofile', 'job', 'keyservermember', 'keyservermonitor', 'keyservermonitorencryptedseed', 'keyservermonitorseed', 'keyservermonitorsek', 'l2domain', 'l2domaintemplate', 'l7applicationsignature', 'ldapconfiguration', 'license', 'licensestatus', 'link', 'location', 'lteinformation', 'ltestatistics', 'macfilterprofile', 'me', 'mirrordestination', 'monitoringport', 'monitorscope', 'multicastchannelmap', 'multicastlist', 'multicastrange', 'multinicvport', 'natmapentry', 'netconfmanager', 'netconfprofile', 'netconfsession', 'networklayout', 'networkmacrogroup', 'networkperformancebinding', 'networkperformancemeasurement', 'nexthop', 'nsgateway', 'nsgatewayscount', 'nsgatewayssummary', 'nsgatewaytemplate', 'nsggroup', 'nsgredundancygroup', 'nsgroutingpolicybinding', 'nsport', 'nsporttemplate', 'nsredundantport', 'ospfarea', 'ospfinstance', 'ospfinterface', 'overlayaddresspool', 'overlaymirrordestination', 'overlaymirrordestinationtemplate', 'overlaypatnatentry', 'patch', 'patnatpool', 'permission', 'policydecision', 'policyentry', 'policygroup', 'policygroupcategory', 'policygrouptemplate', 'policyobjectgroup', 'policystatement', 'port', 'porttemplate', 'psnatpool', 'pspatmap', 'ptranslationmap', 'publicnetwork', 'qos', 'qospolicer', 'ratelimiter', 'redirectiontarget', 'redirectiontargettemplate', 'redundancygroup', 'resync', 'routingpolicy', 'saasapplicationgroup', 'saasapplicationtype', 'sapegressqosprofile', 'sapingressqosprofile', 'service', 'sharednetworkresource', 'shuntlink', 'site', 'spatsourcespool', 'sshkey', 'ssidconnection', 'staticroute', 'statistics', 'statisticscollector', 'statisticspolicy', 'subnet', 'subnettemplate', 'systemconfig', 'tca', 'tier', 'trunk', 'underlay', 'uplinkconnection', 'uplinkroutedistinguisher', 'user', 'usercontext', 'vcenter', 'vcentercluster', 'vcenterdatacenter', 'vcenterhypervisor', 'virtualfirewallpolicy', 'virtualfirewallrule', 'virtualip', 'vlan', 'vlantemplate', 'vm', 'vminterface', 'vnf', 'vnfcatalog', 'vnfdescriptor', 'vnfdomainmapping', 'vnfinterface', 'vnfinterfacedescriptor', 'vnfmetadata', 'vnfthresholdpolicy', 'vpnconnection', 'vport', 'vportmirror', 'vrs', 'vrsaddressrange', 'vrsconfig', 'vsc', 'vsd', 'vsgredundantport', 'vsp', 'wirelessport', 'zfbrequest', 'zone', 'zonetemplate']
    __create_parents__ = ['addressmap', 'addressrange', 'alarm', 'allalarm', 'allgateway', 'allredundancygroup', 'application', 'applicationbinding', 'applicationperformancemanagement', 'applicationperformancemanagementbinding', 'autodiscoveredgateway', 'avatar', 'bfdsession', 'bgpneighbor', 'bgppeer', 'bgpprofile', 'bootstrap', 'bootstrapactivation', 'brconnection', 'bridgeinterface', 'bulkstatistics', 'certificate', 'cms', 'component', 'connectionendpoint', 'container', 'containerinterface', 'containerresync', 'cosremarkingpolicy', 'cosremarkingpolicytable', 'csnatpool', 'ctranslationmap', 'customproperty', 'defaultgateway', 'demarcationservice', 'deploymentfailure', 'destinationurl', 'dhcpoption', 'diskstat', 'domain', 'domaintemplate', 'dscpforwardingclassmapping', 'dscpforwardingclasstable', 'dscpremarkingpolicy', 'dscpremarkingpolicytable', 'ducgroup', 'ducgroupbinding', 'eamconfig', 'egressaclentrytemplate', 'egressacltemplate', 'egressadvfwdentrytemplate', 'egressadvfwdtemplate', 'egressdomainfloatingipaclentrytemplate', 'egressdomainfloatingipacltemplate', 'egressprofile', 'egressqospolicy', 'enterprise', 'enterprisenetwork', 'enterprisepermission', 'enterpriseprofile', 'enterprisesecureddata', 'enterprisesecurity', 'eventlog', 'firewallacl', 'firewallrule', 'floatingip', 'forwardingpathlist', 'forwardingpathlistentry', 'gateway', 'gatewayredundantport', 'gatewaysecureddata', 'gatewaysecurity', 'gatewayslocation', 'gatewaytemplate', 'globalmetadata', 'group', 'groupkeyencryptionprofile', 'hostinterface', 'hsc', 'ikecertificate', 'ikeencryptionprofile', 'ikegateway', 'ikegatewayconfig', 'ikegatewayconnection', 'ikegatewayprofile', 'ikepsk', 'ikesubnet', 'infraconfig', 'infrastructureaccessprofile', 'infrastructureevdfprofile', 'infrastructuregatewayprofile', 'infrastructurevscprofile', 'ingressaclentrytemplate', 'ingressacltemplate', 'ingressadvfwdentrytemplate', 'ingressadvfwdtemplate', 'ingressprofile', 'ingressqospolicy', 'ipfilterprofile', 'ipreservation', 'ipv6filterprofile', 'job', 'keyservermember', 'keyservermonitor', 'keyservermonitorencryptedseed', 'keyservermonitorseed', 'keyservermonitorsek', 'l2domain', 'l2domaintemplate', 'l7applicationsignature', 'ldapconfiguration', 'license', 'licensestatus', 'link', 'location', 'lteinformation', 'ltestatistics', 'macfilterprofile', 'me', 'mirrordestination', 'monitoringport', 'monitorscope', 'multicastchannelmap', 'multicastlist', 'multicastrange', 'multinicvport', 'natmapentry', 'netconfmanager', 'netconfprofile', 'netconfsession', 'networklayout', 'networkmacrogroup', 'networkperformancebinding', 'networkperformancemeasurement', 'nexthop', 'nsgateway', 'nsgatewayscount', 'nsgatewayssummary', 'nsgatewaytemplate', 'nsggroup', 'nsgredundancygroup', 'nsgroutingpolicybinding', 'nsport', 'nsporttemplate', 'nsredundantport', 'ospfarea', 'ospfinstance', 'ospfinterface', 'overlayaddresspool', 'overlaymirrordestination', 'overlaymirrordestinationtemplate', 'overlaypatnatentry', 'patch', 'patnatpool', 'permission', 'policydecision', 'policyentry', 'policygroup', 'policygroupcategory', 'policygrouptemplate', 'policyobjectgroup', 'policystatement', 'port', 'porttemplate', 'psnatpool', 'pspatmap', 'ptranslationmap', 'publicnetwork', 'qos', 'qospolicer', 'ratelimiter', 'redirectiontarget', 'redirectiontargettemplate', 'redundancygroup', 'resync', 'routingpolicy', 'saasapplicationgroup', 'saasapplicationtype', 'sapegressqosprofile', 'sapingressqosprofile', 'service', 'sharednetworkresource', 'shuntlink', 'site', 'spatsourcespool', 'sshkey', 'ssidconnection', 'staticroute', 'statistics', 'statisticscollector', 'statisticspolicy', 'subnet', 'subnettemplate', 'systemconfig', 'tca', 'tier', 'trunk', 'underlay', 'uplinkconnection', 'uplinkroutedistinguisher', 'user', 'usercontext', 'vcenter', 'vcentercluster', 'vcenterdatacenter', 'vcenterhypervisor', 'virtualfirewallpolicy', 'virtualfirewallrule', 'virtualip', 'vlan', 'vlantemplate', 'vm', 'vminterface', 'vnf', 'vnfcatalog', 'vnfdescriptor', 'vnfdomainmapping', 'vnfinterface', 'vnfinterfacedescriptor', 'vnfmetadata', 'vnfthresholdpolicy', 'vpnconnection', 'vport', 'vportmirror', 'vrs', 'vrsaddressrange', 'vrsconfig', 'vsc', 'vsd', 'vsgredundantport', 'vsp', 'wirelessport', 'zfbrequest', 'zone', 'zonetemplate']

    def __init__(self):
        super(NUSimGlobalMetadata, self).__init__()