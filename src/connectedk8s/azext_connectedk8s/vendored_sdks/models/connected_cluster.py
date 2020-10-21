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

from .tracked_resource import TrackedResource


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
     ~azure.mgmt.hybridkubernetes.models.ConnectedClusterIdentity
    :param agent_public_key_certificate: Required. Base64 encoded public
     certificate used by the agent to do the initial handshake to the backend
     services in Azure.
    :type agent_public_key_certificate: str
    :param aad_profile: Required. AAD profile of the connected cluster.
    :type aad_profile:
     ~azure.mgmt.hybridkubernetes.models.ConnectedClusterAADProfile
    :ivar kubernetes_version: The Kubernetes version of the connected cluster
     resource
    :vartype kubernetes_version: str
    :ivar total_node_count: Number of nodes present in the connected cluster
     resource
    :vartype total_node_count: int
    :ivar agent_version: Version of the agent running on the connected cluster
     resource
    :vartype agent_version: str
    :param provisioning_state: Provisioning state of the connected cluster
     resource. Possible values include: 'Succeeded', 'Failed', 'Canceled',
     'Provisioning', 'Updating', 'Deleting', 'Accepted'
    :type provisioning_state: str or
     ~azure.mgmt.hybridkubernetes.models.ProvisioningState
    :param kubernetes_distro: The Kuberenetes distribution on which the agents
     are running
    :type kubernetes_distro: str
    :param kubernetes_infra: The Kubernetes infrastructure on which the agents
     are running
    :type kubernetes_infra: str
    :ivar offering: The 1P service name through which Arc onboarding has
     happened in case of integrated onboarding
    :vartype offering: str
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
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ConnectedClusterIdentity'},
        'agent_public_key_certificate': {'key': 'properties.agentPublicKeyCertificate', 'type': 'str'},
        'aad_profile': {'key': 'properties.aadProfile', 'type': 'ConnectedClusterAADProfile'},
        'kubernetes_version': {'key': 'properties.kubernetesVersion', 'type': 'str'},
        'total_node_count': {'key': 'properties.totalNodeCount', 'type': 'int'},
        'agent_version': {'key': 'properties.agentVersion', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'kubernetes_distro': {'key': 'properties.kubernetesDistro', 'type': 'str'},
        'kubernetes_infra': {'key': 'properties.kubernetesInfra', 'type': 'str'},
        'offering': {'key': 'properties.Offering', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ConnectedCluster, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.agent_public_key_certificate = kwargs.get('agent_public_key_certificate', None)
        self.aad_profile = kwargs.get('aad_profile', None)
        self.kubernetes_version = None
        self.total_node_count = None
        self.agent_version = None
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.kubernetes_distro = kwargs.get('kubernetes_distro', None)
        self.kubernetes_infra = kwargs.get('kubernetes_infra', None)
        self.offering = None
