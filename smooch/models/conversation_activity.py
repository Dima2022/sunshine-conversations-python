# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.27
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConversationActivity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, role=None, type=None, name=None, avatar_url=None):
        """
        ConversationActivity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'role': 'str',
            'type': 'str',
            'name': 'str',
            'avatar_url': 'str'
        }

        self.attribute_map = {
            'role': 'role',
            'type': 'type',
            'name': 'name',
            'avatar_url': 'avatarUrl'
        }

        self._role = None
        self._type = None
        self._name = None
        self._avatar_url = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if role is not None:
          self.role = role
        if type is not None:
          self.type = type
        if name is not None:
          self.name = name
        if avatar_url is not None:
          self.avatar_url = avatar_url

    @property
    def role(self):
        """
        Gets the role of this ConversationActivity.
        The role of the actor. Must be *appMaker*. See [**RoleEnum**](Enums.md#RoleEnum) for available values.

        :return: The role of this ConversationActivity.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this ConversationActivity.
        The role of the actor. Must be *appMaker*. See [**RoleEnum**](Enums.md#RoleEnum) for available values.

        :param role: The role of this ConversationActivity.
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

    @property
    def type(self):
        """
        Gets the type of this ConversationActivity.
        The type of activity to trigger. Must be either *typing:start* or *typing:stop*. See [**MessageTypeEnum**](Enums.md#MessageTypeEnum) for available values.

        :return: The type of this ConversationActivity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ConversationActivity.
        The type of activity to trigger. Must be either *typing:start* or *typing:stop*. See [**MessageTypeEnum**](Enums.md#MessageTypeEnum) for available values.

        :param type: The type of this ConversationActivity.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this ConversationActivity.
        The name of the app maker that starts or stops typing a response.

        :return: The name of this ConversationActivity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConversationActivity.
        The name of the app maker that starts or stops typing a response.

        :param name: The name of this ConversationActivity.
        :type: str
        """

        self._name = name

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this ConversationActivity.
        The avatar URL of the app maker that starts typing a response.

        :return: The avatar_url of this ConversationActivity.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this ConversationActivity.
        The avatar URL of the app maker that starts typing a response.

        :param avatar_url: The avatar_url of this ConversationActivity.
        :type: str
        """

        self._avatar_url = avatar_url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ConversationActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
