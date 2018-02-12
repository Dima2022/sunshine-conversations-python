# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 2.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IntegrationCreate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, page_access_token=None, app_id=None, app_secret=None, account_sid=None, auth_token=None, phone_number_sid=None, token=None, channel_access_token=None, encoding_aes_key=None, from_address=None, certificate=None, password=None, auto_update_badge=None, server_key=None, sender_id=None, consumer_key=None, consumer_secret=None, access_token_key=None, access_token_secret=None, access_key=None, originator=None, brand_color=None, conversation_color=None, action_color=None, display_style=None, button_icon_url=None, integration_order=None, business_name=None, business_icon_url=None):
        """
        IntegrationCreate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'page_access_token': 'str',
            'app_id': 'str',
            'app_secret': 'str',
            'account_sid': 'str',
            'auth_token': 'str',
            'phone_number_sid': 'str',
            'token': 'str',
            'channel_access_token': 'str',
            'encoding_aes_key': 'str',
            'from_address': 'str',
            'certificate': 'str',
            'password': 'str',
            'auto_update_badge': 'bool',
            'server_key': 'str',
            'sender_id': 'str',
            'consumer_key': 'str',
            'consumer_secret': 'str',
            'access_token_key': 'str',
            'access_token_secret': 'str',
            'access_key': 'str',
            'originator': 'str',
            'brand_color': 'str',
            'conversation_color': 'str',
            'action_color': 'str',
            'display_style': 'str',
            'button_icon_url': 'str',
            'integration_order': 'list[str]',
            'business_name': 'str',
            'business_icon_url': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'page_access_token': 'pageAccessToken',
            'app_id': 'appId',
            'app_secret': 'appSecret',
            'account_sid': 'accountSid',
            'auth_token': 'authToken',
            'phone_number_sid': 'phoneNumberSid',
            'token': 'token',
            'channel_access_token': 'channelAccessToken',
            'encoding_aes_key': 'encodingAesKey',
            'from_address': 'fromAddress',
            'certificate': 'certificate',
            'password': 'password',
            'auto_update_badge': 'autoUpdateBadge',
            'server_key': 'serverKey',
            'sender_id': 'senderId',
            'consumer_key': 'consumerKey',
            'consumer_secret': 'consumerSecret',
            'access_token_key': 'accessTokenKey',
            'access_token_secret': 'accessTokenSecret',
            'access_key': 'accessKey',
            'originator': 'originator',
            'brand_color': 'brandColor',
            'conversation_color': 'conversationColor',
            'action_color': 'actionColor',
            'display_style': 'displayStyle',
            'button_icon_url': 'buttonIconUrl',
            'integration_order': 'integrationOrder',
            'business_name': 'businessName',
            'business_icon_url': 'businessIconUrl'
        }

        self._type = None
        self._page_access_token = None
        self._app_id = None
        self._app_secret = None
        self._account_sid = None
        self._auth_token = None
        self._phone_number_sid = None
        self._token = None
        self._channel_access_token = None
        self._encoding_aes_key = None
        self._from_address = None
        self._certificate = None
        self._password = None
        self._auto_update_badge = None
        self._server_key = None
        self._sender_id = None
        self._consumer_key = None
        self._consumer_secret = None
        self._access_token_key = None
        self._access_token_secret = None
        self._access_key = None
        self._originator = None
        self._brand_color = None
        self._conversation_color = None
        self._action_color = None
        self._display_style = None
        self._button_icon_url = None
        self._integration_order = None
        self._business_name = None
        self._business_icon_url = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if type is not None:
          self.type = type
        if page_access_token is not None:
          self.page_access_token = page_access_token
        if app_id is not None:
          self.app_id = app_id
        if app_secret is not None:
          self.app_secret = app_secret
        if account_sid is not None:
          self.account_sid = account_sid
        if auth_token is not None:
          self.auth_token = auth_token
        if phone_number_sid is not None:
          self.phone_number_sid = phone_number_sid
        if token is not None:
          self.token = token
        if channel_access_token is not None:
          self.channel_access_token = channel_access_token
        if encoding_aes_key is not None:
          self.encoding_aes_key = encoding_aes_key
        if from_address is not None:
          self.from_address = from_address
        if certificate is not None:
          self.certificate = certificate
        if password is not None:
          self.password = password
        if auto_update_badge is not None:
          self.auto_update_badge = auto_update_badge
        if server_key is not None:
          self.server_key = server_key
        if sender_id is not None:
          self.sender_id = sender_id
        if consumer_key is not None:
          self.consumer_key = consumer_key
        if consumer_secret is not None:
          self.consumer_secret = consumer_secret
        if access_token_key is not None:
          self.access_token_key = access_token_key
        if access_token_secret is not None:
          self.access_token_secret = access_token_secret
        if access_key is not None:
          self.access_key = access_key
        if originator is not None:
          self.originator = originator
        if brand_color is not None:
          self.brand_color = brand_color
        if conversation_color is not None:
          self.conversation_color = conversation_color
        if action_color is not None:
          self.action_color = action_color
        if display_style is not None:
          self.display_style = display_style
        if button_icon_url is not None:
          self.button_icon_url = button_icon_url
        if integration_order is not None:
          self.integration_order = integration_order
        if business_name is not None:
          self.business_name = business_name
        if business_icon_url is not None:
          self.business_icon_url = business_icon_url

    @property
    def type(self):
        """
        Gets the type of this IntegrationCreate.
        The integration type.

        :return: The type of this IntegrationCreate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IntegrationCreate.
        The integration type.

        :param type: The type of this IntegrationCreate.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def page_access_token(self):
        """
        Gets the page_access_token of this IntegrationCreate.
        Facebook Page Access Token. Required for *messenger* integrations. 

        :return: The page_access_token of this IntegrationCreate.
        :rtype: str
        """
        return self._page_access_token

    @page_access_token.setter
    def page_access_token(self, page_access_token):
        """
        Sets the page_access_token of this IntegrationCreate.
        Facebook Page Access Token. Required for *messenger* integrations. 

        :param page_access_token: The page_access_token of this IntegrationCreate.
        :type: str
        """

        self._page_access_token = page_access_token

    @property
    def app_id(self):
        """
        Gets the app_id of this IntegrationCreate.
        Facebook App ID OR WeChat App ID. Required for *messenger* and *wechat* integrations. 

        :return: The app_id of this IntegrationCreate.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """
        Sets the app_id of this IntegrationCreate.
        Facebook App ID OR WeChat App ID. Required for *messenger* and *wechat* integrations. 

        :param app_id: The app_id of this IntegrationCreate.
        :type: str
        """

        self._app_id = app_id

    @property
    def app_secret(self):
        """
        Gets the app_secret of this IntegrationCreate.
        Facebook Page App Secret OR WeChat App Secret. Required for *messenger* and *wechat* integrations. 

        :return: The app_secret of this IntegrationCreate.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """
        Sets the app_secret of this IntegrationCreate.
        Facebook Page App Secret OR WeChat App Secret. Required for *messenger* and *wechat* integrations. 

        :param app_secret: The app_secret of this IntegrationCreate.
        :type: str
        """

        self._app_secret = app_secret

    @property
    def account_sid(self):
        """
        Gets the account_sid of this IntegrationCreate.
        Twilio Account SID. Required for *twilio* integrations. 

        :return: The account_sid of this IntegrationCreate.
        :rtype: str
        """
        return self._account_sid

    @account_sid.setter
    def account_sid(self, account_sid):
        """
        Sets the account_sid of this IntegrationCreate.
        Twilio Account SID. Required for *twilio* integrations. 

        :param account_sid: The account_sid of this IntegrationCreate.
        :type: str
        """

        self._account_sid = account_sid

    @property
    def auth_token(self):
        """
        Gets the auth_token of this IntegrationCreate.
        Twilio Auth Token. Required for *twilio* integrations. 

        :return: The auth_token of this IntegrationCreate.
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """
        Sets the auth_token of this IntegrationCreate.
        Twilio Auth Token. Required for *twilio* integrations. 

        :param auth_token: The auth_token of this IntegrationCreate.
        :type: str
        """

        self._auth_token = auth_token

    @property
    def phone_number_sid(self):
        """
        Gets the phone_number_sid of this IntegrationCreate.
        SID for specific phone number. Required for *twilio* integrations. 

        :return: The phone_number_sid of this IntegrationCreate.
        :rtype: str
        """
        return self._phone_number_sid

    @phone_number_sid.setter
    def phone_number_sid(self, phone_number_sid):
        """
        Sets the phone_number_sid of this IntegrationCreate.
        SID for specific phone number. Required for *twilio* integrations. 

        :param phone_number_sid: The phone_number_sid of this IntegrationCreate.
        :type: str
        """

        self._phone_number_sid = phone_number_sid

    @property
    def token(self):
        """
        Gets the token of this IntegrationCreate.
        Telegram Bot Token OR Viber Public Account token. Required for *twilio* and *viber* integrations. 

        :return: The token of this IntegrationCreate.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this IntegrationCreate.
        Telegram Bot Token OR Viber Public Account token. Required for *twilio* and *viber* integrations. 

        :param token: The token of this IntegrationCreate.
        :type: str
        """

        self._token = token

    @property
    def channel_access_token(self):
        """
        Gets the channel_access_token of this IntegrationCreate.
        LINE Channel Access Token. Required for *line* integrations. 

        :return: The channel_access_token of this IntegrationCreate.
        :rtype: str
        """
        return self._channel_access_token

    @channel_access_token.setter
    def channel_access_token(self, channel_access_token):
        """
        Sets the channel_access_token of this IntegrationCreate.
        LINE Channel Access Token. Required for *line* integrations. 

        :param channel_access_token: The channel_access_token of this IntegrationCreate.
        :type: str
        """

        self._channel_access_token = channel_access_token

    @property
    def encoding_aes_key(self):
        """
        Gets the encoding_aes_key of this IntegrationCreate.
        AES Encoding Key. (Optional) Used for *wechat* integrations. 

        :return: The encoding_aes_key of this IntegrationCreate.
        :rtype: str
        """
        return self._encoding_aes_key

    @encoding_aes_key.setter
    def encoding_aes_key(self, encoding_aes_key):
        """
        Sets the encoding_aes_key of this IntegrationCreate.
        AES Encoding Key. (Optional) Used for *wechat* integrations. 

        :param encoding_aes_key: The encoding_aes_key of this IntegrationCreate.
        :type: str
        """

        self._encoding_aes_key = encoding_aes_key

    @property
    def from_address(self):
        """
        Gets the from_address of this IntegrationCreate.
        Email will display as coming from this address. (Optional) Used for *frontendEmail* integrations. 

        :return: The from_address of this IntegrationCreate.
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this IntegrationCreate.
        Email will display as coming from this address. (Optional) Used for *frontendEmail* integrations. 

        :param from_address: The from_address of this IntegrationCreate.
        :type: str
        """

        self._from_address = from_address

    @property
    def certificate(self):
        """
        Gets the certificate of this IntegrationCreate.
        The binary of your APN certificate base64 encoded. Required for *apn* integrations. 

        :return: The certificate of this IntegrationCreate.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this IntegrationCreate.
        The binary of your APN certificate base64 encoded. Required for *apn* integrations. 

        :param certificate: The certificate of this IntegrationCreate.
        :type: str
        """

        self._certificate = certificate

    @property
    def password(self):
        """
        Gets the password of this IntegrationCreate.
        The password for your APN certificate. (Optional) Used for *apn* integrations. 

        :return: The password of this IntegrationCreate.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this IntegrationCreate.
        The password for your APN certificate. (Optional) Used for *apn* integrations. 

        :param password: The password of this IntegrationCreate.
        :type: str
        """

        self._password = password

    @property
    def auto_update_badge(self):
        """
        Gets the auto_update_badge of this IntegrationCreate.
        Use the unread count of the conversation as the application badge. (Optional) Used for *apn* integrations. 

        :return: The auto_update_badge of this IntegrationCreate.
        :rtype: bool
        """
        return self._auto_update_badge

    @auto_update_badge.setter
    def auto_update_badge(self, auto_update_badge):
        """
        Sets the auto_update_badge of this IntegrationCreate.
        Use the unread count of the conversation as the application badge. (Optional) Used for *apn* integrations. 

        :param auto_update_badge: The auto_update_badge of this IntegrationCreate.
        :type: bool
        """

        self._auto_update_badge = auto_update_badge

    @property
    def server_key(self):
        """
        Gets the server_key of this IntegrationCreate.
        Your server key from the fcm console. Required for *fcm* integrations. 

        :return: The server_key of this IntegrationCreate.
        :rtype: str
        """
        return self._server_key

    @server_key.setter
    def server_key(self, server_key):
        """
        Sets the server_key of this IntegrationCreate.
        Your server key from the fcm console. Required for *fcm* integrations. 

        :param server_key: The server_key of this IntegrationCreate.
        :type: str
        """

        self._server_key = server_key

    @property
    def sender_id(self):
        """
        Gets the sender_id of this IntegrationCreate.
        Your sender id from the fcm console. Required for *fcm* integrations. 

        :return: The sender_id of this IntegrationCreate.
        :rtype: str
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """
        Sets the sender_id of this IntegrationCreate.
        Your sender id from the fcm console. Required for *fcm* integrations. 

        :param sender_id: The sender_id of this IntegrationCreate.
        :type: str
        """

        self._sender_id = sender_id

    @property
    def consumer_key(self):
        """
        Gets the consumer_key of this IntegrationCreate.
        The consumer key for your Twitter app. Required for *twitter* integrations. 

        :return: The consumer_key of this IntegrationCreate.
        :rtype: str
        """
        return self._consumer_key

    @consumer_key.setter
    def consumer_key(self, consumer_key):
        """
        Sets the consumer_key of this IntegrationCreate.
        The consumer key for your Twitter app. Required for *twitter* integrations. 

        :param consumer_key: The consumer_key of this IntegrationCreate.
        :type: str
        """

        self._consumer_key = consumer_key

    @property
    def consumer_secret(self):
        """
        Gets the consumer_secret of this IntegrationCreate.
        The consumer secret for your Twitter app. Required for *twitter* integrations. 

        :return: The consumer_secret of this IntegrationCreate.
        :rtype: str
        """
        return self._consumer_secret

    @consumer_secret.setter
    def consumer_secret(self, consumer_secret):
        """
        Sets the consumer_secret of this IntegrationCreate.
        The consumer secret for your Twitter app. Required for *twitter* integrations. 

        :param consumer_secret: The consumer_secret of this IntegrationCreate.
        :type: str
        """

        self._consumer_secret = consumer_secret

    @property
    def access_token_key(self):
        """
        Gets the access_token_key of this IntegrationCreate.
        The access token key obtained from your user via oauth. Required for *twitter* integrations. 

        :return: The access_token_key of this IntegrationCreate.
        :rtype: str
        """
        return self._access_token_key

    @access_token_key.setter
    def access_token_key(self, access_token_key):
        """
        Sets the access_token_key of this IntegrationCreate.
        The access token key obtained from your user via oauth. Required for *twitter* integrations. 

        :param access_token_key: The access_token_key of this IntegrationCreate.
        :type: str
        """

        self._access_token_key = access_token_key

    @property
    def access_token_secret(self):
        """
        Gets the access_token_secret of this IntegrationCreate.
        The access token secret obtained from your user via oauth. Required for *twitter* integrations. 

        :return: The access_token_secret of this IntegrationCreate.
        :rtype: str
        """
        return self._access_token_secret

    @access_token_secret.setter
    def access_token_secret(self, access_token_secret):
        """
        Sets the access_token_secret of this IntegrationCreate.
        The access token secret obtained from your user via oauth. Required for *twitter* integrations. 

        :param access_token_secret: The access_token_secret of this IntegrationCreate.
        :type: str
        """

        self._access_token_secret = access_token_secret

    @property
    def access_key(self):
        """
        Gets the access_key of this IntegrationCreate.
        The public API key of your MessageBird account. Required for *messagebird* integrations. 

        :return: The access_key of this IntegrationCreate.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """
        Sets the access_key of this IntegrationCreate.
        The public API key of your MessageBird account. Required for *messagebird* integrations. 

        :param access_key: The access_key of this IntegrationCreate.
        :type: str
        """

        self._access_key = access_key

    @property
    def originator(self):
        """
        Gets the originator of this IntegrationCreate.
        Smooch will receive all messages sent to this phone number. Required for *messagebird* integrations. 

        :return: The originator of this IntegrationCreate.
        :rtype: str
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """
        Sets the originator of this IntegrationCreate.
        Smooch will receive all messages sent to this phone number. Required for *messagebird* integrations. 

        :param originator: The originator of this IntegrationCreate.
        :type: str
        """

        self._originator = originator

    @property
    def brand_color(self):
        """
        Gets the brand_color of this IntegrationCreate.
        This color will be used in the messenger header and the button or tab in idle state. (Optional) Used for *Web Messenger* integrations. 

        :return: The brand_color of this IntegrationCreate.
        :rtype: str
        """
        return self._brand_color

    @brand_color.setter
    def brand_color(self, brand_color):
        """
        Sets the brand_color of this IntegrationCreate.
        This color will be used in the messenger header and the button or tab in idle state. (Optional) Used for *Web Messenger* integrations. 

        :param brand_color: The brand_color of this IntegrationCreate.
        :type: str
        """

        self._brand_color = brand_color

    @property
    def conversation_color(self):
        """
        Gets the conversation_color of this IntegrationCreate.
        This color will be used for customer messages, quick replies and actions in the footer. (Optional) Used for *Web Messenger* integrations. 

        :return: The conversation_color of this IntegrationCreate.
        :rtype: str
        """
        return self._conversation_color

    @conversation_color.setter
    def conversation_color(self, conversation_color):
        """
        Sets the conversation_color of this IntegrationCreate.
        This color will be used for customer messages, quick replies and actions in the footer. (Optional) Used for *Web Messenger* integrations. 

        :param conversation_color: The conversation_color of this IntegrationCreate.
        :type: str
        """

        self._conversation_color = conversation_color

    @property
    def action_color(self):
        """
        Gets the action_color of this IntegrationCreate.
        This color will be used for call-to-actions inside your messages. (Optional) Used for *Web Messenger* integrations. 

        :return: The action_color of this IntegrationCreate.
        :rtype: str
        """
        return self._action_color

    @action_color.setter
    def action_color(self, action_color):
        """
        Sets the action_color of this IntegrationCreate.
        This color will be used for call-to-actions inside your messages. (Optional) Used for *Web Messenger* integrations. 

        :param action_color: The action_color of this IntegrationCreate.
        :type: str
        """

        self._action_color = action_color

    @property
    def display_style(self):
        """
        Gets the display_style of this IntegrationCreate.
        Choose how the messenger will appear on your website. Must be either button or tab. (Optional) Used for *Web Messenger* integrations. 

        :return: The display_style of this IntegrationCreate.
        :rtype: str
        """
        return self._display_style

    @display_style.setter
    def display_style(self, display_style):
        """
        Sets the display_style of this IntegrationCreate.
        Choose how the messenger will appear on your website. Must be either button or tab. (Optional) Used for *Web Messenger* integrations. 

        :param display_style: The display_style of this IntegrationCreate.
        :type: str
        """

        self._display_style = display_style

    @property
    def button_icon_url(self):
        """
        Gets the button_icon_url of this IntegrationCreate.
        With the button style Web Messenger, you have the option of selecting your own button icon. (Optional) Used for *Web Messenger* integrations. 

        :return: The button_icon_url of this IntegrationCreate.
        :rtype: str
        """
        return self._button_icon_url

    @button_icon_url.setter
    def button_icon_url(self, button_icon_url):
        """
        Sets the button_icon_url of this IntegrationCreate.
        With the button style Web Messenger, you have the option of selecting your own button icon. (Optional) Used for *Web Messenger* integrations. 

        :param button_icon_url: The button_icon_url of this IntegrationCreate.
        :type: str
        """

        self._button_icon_url = button_icon_url

    @property
    def integration_order(self):
        """
        Gets the integration_order of this IntegrationCreate.
        A custom business name for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :return: The integration_order of this IntegrationCreate.
        :rtype: list[str]
        """
        return self._integration_order

    @integration_order.setter
    def integration_order(self, integration_order):
        """
        Sets the integration_order of this IntegrationCreate.
        A custom business name for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :param integration_order: The integration_order of this IntegrationCreate.
        :type: list[str]
        """

        self._integration_order = integration_order

    @property
    def business_name(self):
        """
        Gets the business_name of this IntegrationCreate.
        A custom business name for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :return: The business_name of this IntegrationCreate.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """
        Sets the business_name of this IntegrationCreate.
        A custom business name for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :param business_name: The business_name of this IntegrationCreate.
        :type: str
        """

        self._business_name = business_name

    @property
    def business_icon_url(self):
        """
        Gets the business_icon_url of this IntegrationCreate.
        A custom business icon url for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :return: The business_icon_url of this IntegrationCreate.
        :rtype: str
        """
        return self._business_icon_url

    @business_icon_url.setter
    def business_icon_url(self, business_icon_url):
        """
        Sets the business_icon_url of this IntegrationCreate.
        A custom business icon url for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :param business_icon_url: The business_icon_url of this IntegrationCreate.
        :type: str
        """

        self._business_icon_url = business_icon_url

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
        if not isinstance(other, IntegrationCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
