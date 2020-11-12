# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource_py3 import TrackedResource


class ConnectedCluster(TrackedResource):
    """Represents a connected cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param identity: Required. The identity of the connected cluster.
    :type identity:
     ~azure.mgmt.hybridkubernetes.v2020_01_01_preview.models.ConnectedClusterIdentity
    :param agent_public_key_certificate: Required. Base64 encoded public
     certificate used by the agent to do the initial handshake to the backend
     services in Azure.
    :type agent_public_key_certificate: str
    :param api_server_certificate: Base64 encoded Kubernetes API server
     certificate authority data
    :type api_server_certificate: str
    :param aad_profile: Required.
    :type aad_profile:
     ~azure.mgmt.hybridkubernetes.v2020_01_01_preview.models.ConnectedClusterAADProfile
    :ivar kubernetes_version: The Kubernetes version of the connected cluster
     resource
    :vartype kubernetes_version: str
    :ivar total_node_count: Number of nodes present in the connected cluster
     resource
    :vartype total_node_count: int
    :ivar agent_version: Version of the agent running on the connected cluster
     resource
    :vartype agent_version: str
    :param provisioning_state: Possible values include: 'Succeeded', 'Failed',
     'Canceled', 'Provisioning', 'Updating', 'Deleting', 'Accepted'
    :type provisioning_state: str or
     ~azure.mgmt.hybridkubernetes.v2020_01_01_preview.models.ProvisioningState
    :param distribution: The Kuberenetes distribution on which the agents are
     running
    :type distribution: str
    :param infrastructure: The Kubernetes infrastructure on which the agents
     are running
    :type infrastructure: str
    :ivar offering: The 1P service name through which Arc onboarding has
     happened in case of integrated onboarding
    :vartype offering: str
    :ivar msi_certificate_expiry_time: Expiry time of the MSI certificate
    :vartype msi_certificate_expiry_time: datetime
    :ivar last_connectivity_time:
    :vartype last_connectivity_time: str
    :param connectivity_status: Possible values include: 'Connecting',
     'Connected', 'Offline', 'Expired'
    :type connectivity_status: str or
     ~azure.mgmt.hybridkubernetes.v2020_01_01_preview.models.ConnectivityStatus
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'identity': {'required': True},
        'agent_public_key_certificate': {'required': True},
        'aad_profile': {'required': True},
        'kubernetes_version': {'readonly': True},
        'total_node_count': {'readonly': True},
        'agent_version': {'readonly': True},
        'offering': {'readonly': True},
        'msi_certificate_expiry_time': {'readonly': True},
        'last_connectivity_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ConnectedClusterIdentity'},
        'agent_public_key_certificate': {'key': 'properties.agentPublicKeyCertificate', 'type': 'str'},
        'api_server_certificate': {'key': 'properties.apiServerCertificate', 'type': 'str'},
        'aad_profile': {'key': 'properties.aadProfile', 'type': 'ConnectedClusterAADProfile'},
        'kubernetes_version': {'key': 'properties.kubernetesVersion', 'type': 'str'},
        'total_node_count': {'key': 'properties.totalNodeCount', 'type': 'int'},
        'agent_version': {'key': 'properties.agentVersion', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'distribution': {'key': 'properties.distribution', 'type': 'str'},
        'infrastructure': {'key': 'properties.infrastructure', 'type': 'str'},
        'offering': {'key': 'properties.offering', 'type': 'str'},
        'msi_certificate_expiry_time': {'key': 'properties.msiCertificateExpiryTime', 'type': 'iso-8601'},
        'last_connectivity_time': {'key': 'properties.lastConnectivityTime', 'type': 'str'},
        'connectivity_status': {'key': 'properties.connectivityStatus', 'type': 'str'},
    }

    def __init__(self, *, location: str, identity, agent_public_key_certificate: str, aad_profile, tags=None, api_server_certificate: str=None, provisioning_state=None, distribution: str=None, infrastructure: str=None, connectivity_status=None, **kwargs) -> None:
        super(ConnectedCluster, self).__init__(tags=tags, location=location, **kwargs)
        self.identity = identity
        self.agent_public_key_certificate = agent_public_key_certificate
        self.api_server_certificate = api_server_certificate
        self.aad_profile = aad_profile
        self.kubernetes_version = None
        self.total_node_count = None
        self.agent_version = None
        self.provisioning_state = provisioning_state
        self.distribution = distribution
        self.infrastructure = infrastructure
        self.offering = None
        self.msi_certificate_expiry_time = None
        self.last_connectivity_time = None
        self.connectivity_status = connectivity_status
