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

from msrest.serialization import Model


class AuthenticationDetails(Model):
    """AuthenticationDetails.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar authentication_method: Required. The mode of client authentication.
     Default value: "Token" .
    :vartype authentication_method: str
    :param value: Required.
    :type value:
     ~azure.mgmt.hybridkubernetes.v2020_01_01_preview.models.AuthenticationDetailsValue
    """

    _validation = {
        'authentication_method': {'required': True, 'constant': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'authentication_method': {'key': 'authenticationMethod', 'type': 'str'},
        'value': {'key': 'value', 'type': 'AuthenticationDetailsValue'},
    }

    authentication_method = "Token"

    def __init__(self, **kwargs):
        super(AuthenticationDetails, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
