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


class CredentialResult(Model):
    """The credential result response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the credential.
    :vartype name: str
    :ivar value: Base64-encoded Kubernetes configuration file.
    :vartype value: bytearray
    :ivar expiry_time: Expiry time of the credentials.
    :vartype expiry_time: datetime
    """

    _validation = {
        'name': {'readonly': True},
        'value': {'readonly': True},
        'expiry_time': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'bytearray'},
        'expiry_time': {'key': 'expiryTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs) -> None:
        super(CredentialResult, self).__init__(**kwargs)
        self.name = None
        self.value = None
        self.expiry_time = None
