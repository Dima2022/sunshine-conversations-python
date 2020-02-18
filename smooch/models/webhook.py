# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Webhook(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, target=None, triggers=None, secret=None, version=None, include_client=None, include_full_app_user=None):
        """
        Webhook - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'target': 'str',
            'triggers': 'list[str]',
            'secret': 'str',
            'version': 'str',
            'include_client': 'bool',
            'include_full_app_user': 'bool'
        }

        self.attribute_map = {
            'id': '_id',
            'target': 'target',
            'triggers': 'triggers',
            'secret': 'secret',
            'version': 'version',
            'include_client': 'includeClient',
            'include_full_app_user': 'includeFullAppUser'
        }

        self._id = None
        self._target = None
        self._triggers = None
        self._secret = None
        self._version = None
        self._include_client = None
        self._include_full_app_user = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if id is not None:
          self.id = id
        if target is not None:
          self.target = target
        if triggers is not None:
          self.triggers = triggers
        if secret is not None:
          self.secret = secret
        if version is not None:
          self.version = version
        if include_client is not None:
          self.include_client = include_client
        if include_full_app_user is not None:
          self.include_full_app_user = include_full_app_user

    @property
    def id(self):
        """
        Gets the id of this Webhook.
        The webhook ID, generated automatically.

        :return: The id of this Webhook.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Webhook.
        The webhook ID, generated automatically.

        :param id: The id of this Webhook.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def target(self):
        """
        Gets the target of this Webhook.
        URL to be called when the webhook is triggered.

        :return: The target of this Webhook.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this Webhook.
        URL to be called when the webhook is triggered.

        :param target: The target of this Webhook.
        :type: str
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")

        self._target = target

    @property
    def triggers(self):
        """
        Gets the triggers of this Webhook.
        An array of triggers you wish to have the webhook listen to. See [**WebhookTriggersEnum**](Enums.md#WebhookTriggersEnum) for available values.

        :return: The triggers of this Webhook.
        :rtype: list[str]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """
        Sets the triggers of this Webhook.
        An array of triggers you wish to have the webhook listen to. See [**WebhookTriggersEnum**](Enums.md#WebhookTriggersEnum) for available values.

        :param triggers: The triggers of this Webhook.
        :type: list[str]
        """
        if triggers is None:
            raise ValueError("Invalid value for `triggers`, must not be `None`")

        self._triggers = triggers

    @property
    def secret(self):
        """
        Gets the secret of this Webhook.
        Secret which will be transmitted with each webhook invocation and can be used to verify the authenticity of the caller.

        :return: The secret of this Webhook.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this Webhook.
        Secret which will be transmitted with each webhook invocation and can be used to verify the authenticity of the caller.

        :param secret: The secret of this Webhook.
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")

        self._secret = secret

    @property
    def version(self):
        """
        Gets the version of this Webhook.
        The payload version of the webhook.

        :return: The version of this Webhook.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Webhook.
        The payload version of the webhook.

        :param version: The version of this Webhook.
        :type: str
        """

        self._version = version

    @property
    def include_client(self):
        """
        Gets the include_client of this Webhook.
        Specifies whether webhook payloads should include the client information associated with a conversation in webhook events.

        :return: The include_client of this Webhook.
        :rtype: bool
        """
        return self._include_client

    @include_client.setter
    def include_client(self, include_client):
        """
        Sets the include_client of this Webhook.
        Specifies whether webhook payloads should include the client information associated with a conversation in webhook events.

        :param include_client: The include_client of this Webhook.
        :type: bool
        """

        self._include_client = include_client

    @property
    def include_full_app_user(self):
        """
        Gets the include_full_app_user of this Webhook.
        Specifies whether webhook payloads should include the complete appUser schema for appUser events.

        :return: The include_full_app_user of this Webhook.
        :rtype: bool
        """
        return self._include_full_app_user

    @include_full_app_user.setter
    def include_full_app_user(self, include_full_app_user):
        """
        Sets the include_full_app_user of this Webhook.
        Specifies whether webhook payloads should include the complete appUser schema for appUser events.

        :param include_full_app_user: The include_full_app_user of this Webhook.
        :type: bool
        """

        self._include_full_app_user = include_full_app_user

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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
