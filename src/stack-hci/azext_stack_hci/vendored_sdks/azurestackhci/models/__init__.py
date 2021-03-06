# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AvailableOperations
    from ._models_py3 import Cluster
    from ._models_py3 import ClusterList
    from ._models_py3 import ClusterNode
    from ._models_py3 import ClusterReportedProperties
    from ._models_py3 import ClusterUpdate
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import OperationDetail
    from ._models_py3 import OperationDisplay
    from ._models_py3 import Resource
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import AvailableOperations  # type: ignore
    from ._models import Cluster  # type: ignore
    from ._models import ClusterList  # type: ignore
    from ._models import ClusterNode  # type: ignore
    from ._models import ClusterReportedProperties  # type: ignore
    from ._models import ClusterUpdate  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import OperationDetail  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import TrackedResource  # type: ignore

from ._azure_stack_hci_client_enums import (
    ProvisioningState,
    Status,
)

__all__ = [
    'AvailableOperations',
    'Cluster',
    'ClusterList',
    'ClusterNode',
    'ClusterReportedProperties',
    'ClusterUpdate',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'OperationDetail',
    'OperationDisplay',
    'Resource',
    'TrackedResource',
    'ProvisioningState',
    'Status',
]
