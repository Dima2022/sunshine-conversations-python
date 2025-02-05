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


class AttachmentMediaTokenBody(object):
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
        'paths': 'list[str]'
    }

    attribute_map = {
        'paths': 'paths'
    }

    nulls = set()

    def __init__(self, paths=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentMediaTokenBody - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._paths = None
        self.discriminator = None

        self.paths = paths

    @property
    def paths(self):
        """Gets the paths of this AttachmentMediaTokenBody.  # noqa: E501

        An array of strings representing the list of attachment paths used to generate the media JWT. One token will be generated for each path. Each token will be valid for 2 hours by default. This value can be modified, see [App Settings](#operation/createApp) for more information.  # noqa: E501

        :return: The paths of this AttachmentMediaTokenBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this AttachmentMediaTokenBody.

        An array of strings representing the list of attachment paths used to generate the media JWT. One token will be generated for each path. Each token will be valid for 2 hours by default. This value can be modified, see [App Settings](#operation/createApp) for more information.  # noqa: E501

        :param paths: The paths of this AttachmentMediaTokenBody.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and paths is None:  # noqa: E501
            raise ValueError("Invalid value for `paths`, must not be `None`")  # noqa: E501

        self._paths = paths

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
        if not isinstance(other, AttachmentMediaTokenBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentMediaTokenBody):
            return True

        return self.to_dict() != other.to_dict()
