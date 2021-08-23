# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class WhatsAppUpdate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'display_name': 'str',
        'hsm_fallback_language': 'str',
        'account_id': 'str',
        'account_management_access_token': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'hsm_fallback_language': 'hsmFallbackLanguage',
        'account_id': 'accountId',
        'account_management_access_token': 'accountManagementAccessToken'
    }

    nulls = set()

    def __init__(self, display_name=Undefined(), hsm_fallback_language='en_US', account_id=Undefined(), account_management_access_token=Undefined(), local_vars_configuration=None):  # noqa: E501
        """WhatsAppUpdate - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._hsm_fallback_language = None
        self._account_id = None
        self._account_management_access_token = None
        self.discriminator = None

        self.display_name = display_name
        self.hsm_fallback_language = hsm_fallback_language
        self.account_id = account_id
        self.account_management_access_token = account_management_access_token

    @property
    def display_name(self):
        """Gets the display_name of this WhatsAppUpdate.  # noqa: E501

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :return: The display_name of this WhatsAppUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this WhatsAppUpdate.

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :param display_name: The display_name of this WhatsAppUpdate.  # noqa: E501
        :type: str
        """
        if type(display_name) is Undefined:
            display_name = None
            self.nulls.discard("display_name")
        elif display_name is None:
            self.nulls.add("display_name")
        else:
            self.nulls.discard("display_name")
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 100):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def hsm_fallback_language(self):
        """Gets the hsm_fallback_language of this WhatsAppUpdate.  # noqa: E501

        Specify a fallback language to use when sending WhatsApp message template using the short hand syntax. Defaults to en_US. See WhatsApp documentation for more info.  # noqa: E501

        :return: The hsm_fallback_language of this WhatsAppUpdate.  # noqa: E501
        :rtype: str
        """
        return self._hsm_fallback_language

    @hsm_fallback_language.setter
    def hsm_fallback_language(self, hsm_fallback_language):
        """Sets the hsm_fallback_language of this WhatsAppUpdate.

        Specify a fallback language to use when sending WhatsApp message template using the short hand syntax. Defaults to en_US. See WhatsApp documentation for more info.  # noqa: E501

        :param hsm_fallback_language: The hsm_fallback_language of this WhatsAppUpdate.  # noqa: E501
        :type: str
        """
        if type(hsm_fallback_language) is Undefined:
            hsm_fallback_language = None
            self.nulls.discard("hsm_fallback_language")
        elif hsm_fallback_language is None:
            self.nulls.add("hsm_fallback_language")
        else:
            self.nulls.discard("hsm_fallback_language")

        self._hsm_fallback_language = hsm_fallback_language

    @property
    def account_id(self):
        """Gets the account_id of this WhatsAppUpdate.  # noqa: E501

        The business ID associated with the WhatsApp account. In combination with accountManagementAccessToken, it’s used for Message Template Reconstruction.  # noqa: E501

        :return: The account_id of this WhatsAppUpdate.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this WhatsAppUpdate.

        The business ID associated with the WhatsApp account. In combination with accountManagementAccessToken, it’s used for Message Template Reconstruction.  # noqa: E501

        :param account_id: The account_id of this WhatsAppUpdate.  # noqa: E501
        :type: str
        """
        if type(account_id) is Undefined:
            account_id = None
            self.nulls.discard("account_id")
        elif account_id is None:
            self.nulls.add("account_id")
        else:
            self.nulls.discard("account_id")

        self._account_id = account_id

    @property
    def account_management_access_token(self):
        """Gets the account_management_access_token of this WhatsAppUpdate.  # noqa: E501

        An access token associated with the accountId used to query the WhatsApp Account Management API. In combination with accountId, it’s used for Message Template Reconstruction.  # noqa: E501

        :return: The account_management_access_token of this WhatsAppUpdate.  # noqa: E501
        :rtype: str
        """
        return self._account_management_access_token

    @account_management_access_token.setter
    def account_management_access_token(self, account_management_access_token):
        """Sets the account_management_access_token of this WhatsAppUpdate.

        An access token associated with the accountId used to query the WhatsApp Account Management API. In combination with accountId, it’s used for Message Template Reconstruction.  # noqa: E501

        :param account_management_access_token: The account_management_access_token of this WhatsAppUpdate.  # noqa: E501
        :type: str
        """
        if type(account_management_access_token) is Undefined:
            account_management_access_token = None
            self.nulls.discard("account_management_access_token")
        elif account_management_access_token is None:
            self.nulls.add("account_management_access_token")
        else:
            self.nulls.discard("account_management_access_token")

        self._account_management_access_token = account_management_access_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WhatsAppUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WhatsAppUpdate):
            return True

        return self.to_dict() != other.to_dict()
