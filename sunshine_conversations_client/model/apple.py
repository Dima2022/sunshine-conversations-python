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

try:
    Integration = __import__("sunshine_conversations_client.model."+re.sub(r'(?<!^)(?=[A-Z])', '_', "Integration").lower(), fromlist=("Integration")).Integration
except ImportError:
    pass

class Apple(Integration):
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
        'type': 'str',
        'business_id': 'str',
        'api_secret': 'str',
        'msp_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'business_id': 'businessId',
        'api_secret': 'apiSecret',
        'msp_id': 'mspId'
    }

    nulls = set()

    def __init__(self, type='apple', business_id=None, api_secret=None, msp_id=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """Apple - a model defined in OpenAPI"""  # noqa: E501
        super().__init__(**kwargs)

        if (super().openapi_types is not None):
            all_types = super().openapi_types.copy()
            all_types.update(self.openapi_types)
            self.openapi_types = all_types

        if (super().attribute_map is not None):
            all_attributes = super().attribute_map.copy()
            all_attributes.update(self.attribute_map)
            self.attribute_map = all_attributes
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._business_id = None
        self._api_secret = None
        self._msp_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.business_id = business_id
        if api_secret is not None:
            self.api_secret = api_secret
        self.msp_id = msp_id

    @property
    def type(self):
        """Gets the type of this Apple.  # noqa: E501

        To configure an Apple Business Chat integration, acquire the required information and call the Create Integration endpoint.   # noqa: E501

        :return: The type of this Apple.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Apple.

        To configure an Apple Business Chat integration, acquire the required information and call the Create Integration endpoint.   # noqa: E501

        :param type: The type of this Apple.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def business_id(self):
        """Gets the business_id of this Apple.  # noqa: E501

        Apple Business Chat ID.  # noqa: E501

        :return: The business_id of this Apple.  # noqa: E501
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this Apple.

        Apple Business Chat ID.  # noqa: E501

        :param business_id: The business_id of this Apple.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and business_id is None:  # noqa: E501
            raise ValueError("Invalid value for `business_id`, must not be `None`")  # noqa: E501

        self._business_id = business_id

    @property
    def api_secret(self):
        """Gets the api_secret of this Apple.  # noqa: E501

        Your Apple API secret which is tied to your Messaging Service Provider.  # noqa: E501

        :return: The api_secret of this Apple.  # noqa: E501
        :rtype: str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        """Sets the api_secret of this Apple.

        Your Apple API secret which is tied to your Messaging Service Provider.  # noqa: E501

        :param api_secret: The api_secret of this Apple.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `api_secret`, must not be `None`")  # noqa: E501

        self._api_secret = api_secret

    @property
    def msp_id(self):
        """Gets the msp_id of this Apple.  # noqa: E501

        Your Messaging Service Provider ID.  # noqa: E501

        :return: The msp_id of this Apple.  # noqa: E501
        :rtype: str
        """
        return self._msp_id

    @msp_id.setter
    def msp_id(self, msp_id):
        """Sets the msp_id of this Apple.

        Your Messaging Service Provider ID.  # noqa: E501

        :param msp_id: The msp_id of this Apple.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and msp_id is None:  # noqa: E501
            raise ValueError("Invalid value for `msp_id`, must not be `None`")  # noqa: E501

        self._msp_id = msp_id

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
        if not isinstance(other, Apple):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Apple):
            return True

        return self.to_dict() != other.to_dict()
