# coding: utf-8

"""
    Smooch

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MessagePost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, role=None, type=None, name=None, email=None, avatar_url=None, metadata=None, payload=None, text=None, media_url=None, media_type=None, items=None, actions=None, destination=None):
        """
        MessagePost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'role': 'str',
            'type': 'str',
            'name': 'str',
            'email': 'str',
            'avatar_url': 'str',
            'metadata': 'object',
            'payload': 'str',
            'text': 'str',
            'media_url': 'str',
            'media_type': 'str',
            'items': 'list[MessageItem]',
            'actions': 'list[Action]',
            'destination': 'Destination'
        }

        self.attribute_map = {
            'role': 'role',
            'type': 'type',
            'name': 'name',
            'email': 'email',
            'avatar_url': 'avatarUrl',
            'metadata': 'metadata',
            'payload': 'payload',
            'text': 'text',
            'media_url': 'mediaUrl',
            'media_type': 'mediaType',
            'items': 'items',
            'actions': 'actions',
            'destination': 'destination'
        }

        self._role = role
        self._type = type
        self._name = name
        self._email = email
        self._avatar_url = avatar_url
        self._metadata = metadata
        self._payload = payload
        self._text = text
        self._media_url = media_url
        self._media_type = media_type
        self._items = items
        self._actions = actions
        self._destination = destination

    @property
    def role(self):
        """
        Gets the role of this MessagePost.

        :return: The role of this MessagePost.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this MessagePost.

        :param role: The role of this MessagePost.
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

    @property
    def type(self):
        """
        Gets the type of this MessagePost.

        :return: The type of this MessagePost.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MessagePost.

        :param type: The type of this MessagePost.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this MessagePost.

        :return: The name of this MessagePost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MessagePost.

        :param name: The name of this MessagePost.
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """
        Gets the email of this MessagePost.

        :return: The email of this MessagePost.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this MessagePost.

        :param email: The email of this MessagePost.
        :type: str
        """

        self._email = email

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this MessagePost.

        :return: The avatar_url of this MessagePost.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this MessagePost.

        :param avatar_url: The avatar_url of this MessagePost.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def metadata(self):
        """
        Gets the metadata of this MessagePost.

        :return: The metadata of this MessagePost.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this MessagePost.

        :param metadata: The metadata of this MessagePost.
        :type: object
        """

        self._metadata = metadata

    @property
    def payload(self):
        """
        Gets the payload of this MessagePost.

        :return: The payload of this MessagePost.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this MessagePost.

        :param payload: The payload of this MessagePost.
        :type: str
        """

        self._payload = payload

    @property
    def text(self):
        """
        Gets the text of this MessagePost.

        :return: The text of this MessagePost.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this MessagePost.

        :param text: The text of this MessagePost.
        :type: str
        """

        self._text = text

    @property
    def media_url(self):
        """
        Gets the media_url of this MessagePost.

        :return: The media_url of this MessagePost.
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """
        Sets the media_url of this MessagePost.

        :param media_url: The media_url of this MessagePost.
        :type: str
        """

        self._media_url = media_url

    @property
    def media_type(self):
        """
        Gets the media_type of this MessagePost.

        :return: The media_type of this MessagePost.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this MessagePost.

        :param media_type: The media_type of this MessagePost.
        :type: str
        """

        self._media_type = media_type

    @property
    def items(self):
        """
        Gets the items of this MessagePost.

        :return: The items of this MessagePost.
        :rtype: list[MessageItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this MessagePost.

        :param items: The items of this MessagePost.
        :type: list[MessageItem]
        """

        self._items = items

    @property
    def actions(self):
        """
        Gets the actions of this MessagePost.

        :return: The actions of this MessagePost.
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this MessagePost.

        :param actions: The actions of this MessagePost.
        :type: list[Action]
        """

        self._actions = actions

    @property
    def destination(self):
        """
        Gets the destination of this MessagePost.
        Specifies which channel to deliver a message to. See [list integrations](https://docs.smooch.io/rest/#list-integrations) to get integration ID and type.

        :return: The destination of this MessagePost.
        :rtype: Destination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this MessagePost.
        Specifies which channel to deliver a message to. See [list integrations](https://docs.smooch.io/rest/#list-integrations) to get integration ID and type.

        :param destination: The destination of this MessagePost.
        :type: Destination
        """

        self._destination = destination

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
        if not isinstance(other, MessagePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
