# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 3.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Action(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, text=None, payload=None, metadata=None, amount=None, currency=None, default=None, icon_url=None, uri=None, fallback=None, size=None, extra_channel_options=None):
        """
        Action - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'text': 'str',
            'payload': 'str',
            'metadata': 'object',
            'amount': 'int',
            'currency': 'str',
            'default': 'bool',
            'icon_url': 'str',
            'uri': 'str',
            'fallback': 'str',
            'size': 'str',
            'extra_channel_options': 'object'
        }

        self.attribute_map = {
            'type': 'type',
            'text': 'text',
            'payload': 'payload',
            'metadata': 'metadata',
            'amount': 'amount',
            'currency': 'currency',
            'default': 'default',
            'icon_url': 'iconUrl',
            'uri': 'uri',
            'fallback': 'fallback',
            'size': 'size',
            'extra_channel_options': 'extraChannelOptions'
        }

        self._type = None
        self._text = None
        self._payload = None
        self._metadata = None
        self._amount = None
        self._currency = None
        self._default = None
        self._icon_url = None
        self._uri = None
        self._fallback = None
        self._size = None
        self._extra_channel_options = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if type is not None:
          self.type = type
        if text is not None:
          self.text = text
        if payload is not None:
          self.payload = payload
        if metadata is not None:
          self.metadata = metadata
        if amount is not None:
          self.amount = amount
        if currency is not None:
          self.currency = currency
        if default is not None:
          self.default = default
        if icon_url is not None:
          self.icon_url = icon_url
        if uri is not None:
          self.uri = uri
        if fallback is not None:
          self.fallback = fallback
        if size is not None:
          self.size = size
        if extra_channel_options is not None:
          self.extra_channel_options = extra_channel_options

    @property
    def type(self):
        """
        Gets the type of this Action.
        The action type.

        :return: The type of this Action.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Action.
        The action type.

        :param type: The type of this Action.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def text(self):
        """
        Gets the text of this Action.
        The button text.

        :return: The text of this Action.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Action.
        The button text.

        :param text: The text of this Action.
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

    @property
    def payload(self):
        """
        Gets the payload of this Action.
        The payload to be sent with the resulting webhook. Required for *postback* and *reply* actions. 

        :return: The payload of this Action.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this Action.
        The payload to be sent with the resulting webhook. Required for *postback* and *reply* actions. 

        :param payload: The payload of this Action.
        :type: str
        """

        self._payload = payload

    @property
    def metadata(self):
        """
        Gets the metadata of this Action.
        Flat JSON object containing any custom properties associated with the action.

        :return: The metadata of this Action.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Action.
        Flat JSON object containing any custom properties associated with the action.

        :param metadata: The metadata of this Action.
        :type: object
        """

        self._metadata = metadata

    @property
    def amount(self):
        """
        Gets the amount of this Action.
        The amount being charged. It needs to be specified in cents and is an integer. Required for *buy* actions. 

        :return: The amount of this Action.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Action.
        The amount being charged. It needs to be specified in cents and is an integer. Required for *buy* actions. 

        :param amount: The amount of this Action.
        :type: int
        """

        self._amount = amount

    @property
    def currency(self):
        """
        Gets the currency of this Action.
        The currency of the amount being charged (USD, CAD, etc.).

        :return: The currency of this Action.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Action.
        The currency of the amount being charged (USD, CAD, etc.).

        :param currency: The currency of this Action.
        :type: str
        """

        self._currency = currency

    @property
    def default(self):
        """
        Gets the default of this Action.
        Flag indicating if the message action is the default for a message item in Facebook Messenger.

        :return: The default of this Action.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this Action.
        Flag indicating if the message action is the default for a message item in Facebook Messenger.

        :param default: The default of this Action.
        :type: bool
        """

        self._default = default

    @property
    def icon_url(self):
        """
        Gets the icon_url of this Action.
        An icon to render next to the reply option (Facebook Messenger and Web Messenger only).

        :return: The icon_url of this Action.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """
        Sets the icon_url of this Action.
        An icon to render next to the reply option (Facebook Messenger and Web Messenger only).

        :param icon_url: The icon_url of this Action.
        :type: str
        """

        self._icon_url = icon_url

    @property
    def uri(self):
        """
        Gets the uri of this Action.
        The action URI. This is the link that will be used in the clients when clicking the button. Required for *link* and *webview* actions. 

        :return: The uri of this Action.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Action.
        The action URI. This is the link that will be used in the clients when clicking the button. Required for *link* and *webview* actions. 

        :param uri: The uri of this Action.
        :type: str
        """

        self._uri = uri

    @property
    def fallback(self):
        """
        Gets the fallback of this Action.
        The webview action fallback uri. This is the link that will be used in clients that do not support webviews. Required for *webview* actions. 

        :return: The fallback of this Action.
        :rtype: str
        """
        return self._fallback

    @fallback.setter
    def fallback(self, fallback):
        """
        Sets the fallback of this Action.
        The webview action fallback uri. This is the link that will be used in clients that do not support webviews. Required for *webview* actions. 

        :param fallback: The fallback of this Action.
        :type: str
        """

        self._fallback = fallback

    @property
    def size(self):
        """
        Gets the size of this Action.
        The size used to display the webview. Allowed values are [\"compact\", \"tall\", \"full\"]. (Optional) Used for *webview* actions. 

        :return: The size of this Action.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Action.
        The size used to display the webview. Allowed values are [\"compact\", \"tall\", \"full\"]. (Optional) Used for *webview* actions. 

        :param size: The size of this Action.
        :type: str
        """

        self._size = size

    @property
    def extra_channel_options(self):
        """
        Gets the extra_channel_options of this Action.
        Extra options to pass directly to the channel API. See [Extra Channel Options](https://docs.smooch.io/rest#extra-channel-options-schema)

        :return: The extra_channel_options of this Action.
        :rtype: object
        """
        return self._extra_channel_options

    @extra_channel_options.setter
    def extra_channel_options(self, extra_channel_options):
        """
        Sets the extra_channel_options of this Action.
        Extra options to pass directly to the channel API. See [Extra Channel Options](https://docs.smooch.io/rest#extra-channel-options-schema)

        :param extra_channel_options: The extra_channel_options of this Action.
        :type: object
        """

        self._extra_channel_options = extra_channel_options

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
        if not isinstance(other, Action):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
