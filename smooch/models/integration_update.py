# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IntegrationUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, brand_color=None, fixed_intro_pane=None, conversation_color=None, action_color=None, display_style=None, button_icon_url=None, button_width=None, button_height=None, integration_order=None, business_name=None, business_icon_url=None, background_image_url=None, origin_whitelist=None, channel_id=None, channel_secret=None, hsm_fallback_language=None):
        """
        IntegrationUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'brand_color': 'str',
            'fixed_intro_pane': 'bool',
            'conversation_color': 'str',
            'action_color': 'str',
            'display_style': 'str',
            'button_icon_url': 'str',
            'button_width': 'str',
            'button_height': 'str',
            'integration_order': 'list[str]',
            'business_name': 'str',
            'business_icon_url': 'str',
            'background_image_url': 'str',
            'origin_whitelist': 'list[str]',
            'channel_id': 'str',
            'channel_secret': 'str',
            'hsm_fallback_language': 'str'
        }

        self.attribute_map = {
            'brand_color': 'brandColor',
            'fixed_intro_pane': 'fixedIntroPane',
            'conversation_color': 'conversationColor',
            'action_color': 'actionColor',
            'display_style': 'displayStyle',
            'button_icon_url': 'buttonIconUrl',
            'button_width': 'buttonWidth',
            'button_height': 'buttonHeight',
            'integration_order': 'integrationOrder',
            'business_name': 'businessName',
            'business_icon_url': 'businessIconUrl',
            'background_image_url': 'backgroundImageUrl',
            'origin_whitelist': 'originWhitelist',
            'channel_id': 'channelId',
            'channel_secret': 'channelSecret',
            'hsm_fallback_language': 'hsmFallbackLanguage'
        }

        self._brand_color = None
        self._fixed_intro_pane = None
        self._conversation_color = None
        self._action_color = None
        self._display_style = None
        self._button_icon_url = None
        self._button_width = None
        self._button_height = None
        self._integration_order = None
        self._business_name = None
        self._business_icon_url = None
        self._background_image_url = None
        self._origin_whitelist = None
        self._channel_id = None
        self._channel_secret = None
        self._hsm_fallback_language = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if brand_color is not None:
          self.brand_color = brand_color
        if fixed_intro_pane is not None:
          self.fixed_intro_pane = fixed_intro_pane
        if conversation_color is not None:
          self.conversation_color = conversation_color
        if action_color is not None:
          self.action_color = action_color
        if display_style is not None:
          self.display_style = display_style
        if button_icon_url is not None:
          self.button_icon_url = button_icon_url
        if button_width is not None:
          self.button_width = button_width
        if button_height is not None:
          self.button_height = button_height
        if integration_order is not None:
          self.integration_order = integration_order
        if business_name is not None:
          self.business_name = business_name
        if business_icon_url is not None:
          self.business_icon_url = business_icon_url
        if background_image_url is not None:
          self.background_image_url = background_image_url
        if origin_whitelist is not None:
          self.origin_whitelist = origin_whitelist
        if channel_id is not None:
          self.channel_id = channel_id
        if channel_secret is not None:
          self.channel_secret = channel_secret
        if hsm_fallback_language is not None:
          self.hsm_fallback_language = hsm_fallback_language

    @property
    def brand_color(self):
        """
        Gets the brand_color of this IntegrationUpdate.
        This color will be used in the messenger header and the button or tab in idle state. (Optional) Used for *Web Messenger* integrations. 

        :return: The brand_color of this IntegrationUpdate.
        :rtype: str
        """
        return self._brand_color

    @brand_color.setter
    def brand_color(self, brand_color):
        """
        Sets the brand_color of this IntegrationUpdate.
        This color will be used in the messenger header and the button or tab in idle state. (Optional) Used for *Web Messenger* integrations. 

        :param brand_color: The brand_color of this IntegrationUpdate.
        :type: str
        """

        self._brand_color = brand_color

    @property
    def fixed_intro_pane(self):
        """
        Gets the fixed_intro_pane of this IntegrationUpdate.
        When `true`, the introduction pane will be pinned at the top of the conversation instead of scrolling with it. The default value is `false`. (Optional) Used for *Web Messenger* integrations. 

        :return: The fixed_intro_pane of this IntegrationUpdate.
        :rtype: bool
        """
        return self._fixed_intro_pane

    @fixed_intro_pane.setter
    def fixed_intro_pane(self, fixed_intro_pane):
        """
        Sets the fixed_intro_pane of this IntegrationUpdate.
        When `true`, the introduction pane will be pinned at the top of the conversation instead of scrolling with it. The default value is `false`. (Optional) Used for *Web Messenger* integrations. 

        :param fixed_intro_pane: The fixed_intro_pane of this IntegrationUpdate.
        :type: bool
        """

        self._fixed_intro_pane = fixed_intro_pane

    @property
    def conversation_color(self):
        """
        Gets the conversation_color of this IntegrationUpdate.
        This color will be used for customer messages, quick replies and actions in the footer. (Optional) Used for *Web Messenger* integrations. 

        :return: The conversation_color of this IntegrationUpdate.
        :rtype: str
        """
        return self._conversation_color

    @conversation_color.setter
    def conversation_color(self, conversation_color):
        """
        Sets the conversation_color of this IntegrationUpdate.
        This color will be used for customer messages, quick replies and actions in the footer. (Optional) Used for *Web Messenger* integrations. 

        :param conversation_color: The conversation_color of this IntegrationUpdate.
        :type: str
        """

        self._conversation_color = conversation_color

    @property
    def action_color(self):
        """
        Gets the action_color of this IntegrationUpdate.
        This color will be used for call-to-actions inside your messages. (Optional) Used for *Web Messenger* integrations. 

        :return: The action_color of this IntegrationUpdate.
        :rtype: str
        """
        return self._action_color

    @action_color.setter
    def action_color(self, action_color):
        """
        Sets the action_color of this IntegrationUpdate.
        This color will be used for call-to-actions inside your messages. (Optional) Used for *Web Messenger* integrations. 

        :param action_color: The action_color of this IntegrationUpdate.
        :type: str
        """

        self._action_color = action_color

    @property
    def display_style(self):
        """
        Gets the display_style of this IntegrationUpdate.
        Choose how the messenger will appear on your website. Must be either button or tab. (Optional) Used for *Web Messenger* integrations. 

        :return: The display_style of this IntegrationUpdate.
        :rtype: str
        """
        return self._display_style

    @display_style.setter
    def display_style(self, display_style):
        """
        Sets the display_style of this IntegrationUpdate.
        Choose how the messenger will appear on your website. Must be either button or tab. (Optional) Used for *Web Messenger* integrations. 

        :param display_style: The display_style of this IntegrationUpdate.
        :type: str
        """

        self._display_style = display_style

    @property
    def button_icon_url(self):
        """
        Gets the button_icon_url of this IntegrationUpdate.
        With the button style Web Messenger, you have the option of selecting your own button icon. (Optional) Used for *Web Messenger* integrations. 

        :return: The button_icon_url of this IntegrationUpdate.
        :rtype: str
        """
        return self._button_icon_url

    @button_icon_url.setter
    def button_icon_url(self, button_icon_url):
        """
        Sets the button_icon_url of this IntegrationUpdate.
        With the button style Web Messenger, you have the option of selecting your own button icon. (Optional) Used for *Web Messenger* integrations. 

        :param button_icon_url: The button_icon_url of this IntegrationUpdate.
        :type: str
        """

        self._button_icon_url = button_icon_url

    @property
    def button_width(self):
        """
        Gets the button_width of this IntegrationUpdate.
        With the button style Web Messenger, you have the option of specifying its width. (Optional) Used for *Web Messenger* integrations. 

        :return: The button_width of this IntegrationUpdate.
        :rtype: str
        """
        return self._button_width

    @button_width.setter
    def button_width(self, button_width):
        """
        Sets the button_width of this IntegrationUpdate.
        With the button style Web Messenger, you have the option of specifying its width. (Optional) Used for *Web Messenger* integrations. 

        :param button_width: The button_width of this IntegrationUpdate.
        :type: str
        """

        self._button_width = button_width

    @property
    def button_height(self):
        """
        Gets the button_height of this IntegrationUpdate.
        With the button style Web Messenger, you have the option of specifying its height. (Optional) Used for *Web Messenger* integrations. 

        :return: The button_height of this IntegrationUpdate.
        :rtype: str
        """
        return self._button_height

    @button_height.setter
    def button_height(self, button_height):
        """
        Sets the button_height of this IntegrationUpdate.
        With the button style Web Messenger, you have the option of specifying its height. (Optional) Used for *Web Messenger* integrations. 

        :param button_height: The button_height of this IntegrationUpdate.
        :type: str
        """

        self._button_height = button_height

    @property
    def integration_order(self):
        """
        Gets the integration_order of this IntegrationUpdate.
        Array of integration IDs, order will be reflected in the Web Messenger. When set, only integrations from this list will be displayed in the Web Messenger. If unset, all integrations will be displayed (Optional) Used for *Web Messenger* integrations. 

        :return: The integration_order of this IntegrationUpdate.
        :rtype: list[str]
        """
        return self._integration_order

    @integration_order.setter
    def integration_order(self, integration_order):
        """
        Sets the integration_order of this IntegrationUpdate.
        Array of integration IDs, order will be reflected in the Web Messenger. When set, only integrations from this list will be displayed in the Web Messenger. If unset, all integrations will be displayed (Optional) Used for *Web Messenger* integrations. 

        :param integration_order: The integration_order of this IntegrationUpdate.
        :type: list[str]
        """

        self._integration_order = integration_order

    @property
    def business_name(self):
        """
        Gets the business_name of this IntegrationUpdate.
        A custom business name for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :return: The business_name of this IntegrationUpdate.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """
        Sets the business_name of this IntegrationUpdate.
        A custom business name for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :param business_name: The business_name of this IntegrationUpdate.
        :type: str
        """

        self._business_name = business_name

    @property
    def business_icon_url(self):
        """
        Gets the business_icon_url of this IntegrationUpdate.
        A custom business icon url for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :return: The business_icon_url of this IntegrationUpdate.
        :rtype: str
        """
        return self._business_icon_url

    @business_icon_url.setter
    def business_icon_url(self, business_icon_url):
        """
        Sets the business_icon_url of this IntegrationUpdate.
        A custom business icon url for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :param business_icon_url: The business_icon_url of this IntegrationUpdate.
        :type: str
        """

        self._business_icon_url = business_icon_url

    @property
    def background_image_url(self):
        """
        Gets the background_image_url of this IntegrationUpdate.
        A custom background url for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :return: The background_image_url of this IntegrationUpdate.
        :rtype: str
        """
        return self._background_image_url

    @background_image_url.setter
    def background_image_url(self, background_image_url):
        """
        Sets the background_image_url of this IntegrationUpdate.
        A custom background url for the Web Messenger. (Optional) Used for *Web Messenger* integrations. 

        :param background_image_url: The background_image_url of this IntegrationUpdate.
        :type: str
        """

        self._background_image_url = background_image_url

    @property
    def origin_whitelist(self):
        """
        Gets the origin_whitelist of this IntegrationUpdate.
        A list of origins to whitelist. When set, only the origins from this list will be able to initialize the Web Messenger. If unset, all origins are whitelisted. The elements in the list should follow the serialized-origin format from RFC 6454 `scheme \"://\" host [ \":\" port ]`, where scheme is `http` or `https`. (Optional) Used for *Web Messenger* integrations. 

        :return: The origin_whitelist of this IntegrationUpdate.
        :rtype: list[str]
        """
        return self._origin_whitelist

    @origin_whitelist.setter
    def origin_whitelist(self, origin_whitelist):
        """
        Sets the origin_whitelist of this IntegrationUpdate.
        A list of origins to whitelist. When set, only the origins from this list will be able to initialize the Web Messenger. If unset, all origins are whitelisted. The elements in the list should follow the serialized-origin format from RFC 6454 `scheme \"://\" host [ \":\" port ]`, where scheme is `http` or `https`. (Optional) Used for *Web Messenger* integrations. 

        :param origin_whitelist: The origin_whitelist of this IntegrationUpdate.
        :type: list[str]
        """

        self._origin_whitelist = origin_whitelist

    @property
    def channel_id(self):
        """
        Gets the channel_id of this IntegrationUpdate.
        LINE Channel ID. Required for *line* integrations. 

        :return: The channel_id of this IntegrationUpdate.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """
        Sets the channel_id of this IntegrationUpdate.
        LINE Channel ID. Required for *line* integrations. 

        :param channel_id: The channel_id of this IntegrationUpdate.
        :type: str
        """

        self._channel_id = channel_id

    @property
    def channel_secret(self):
        """
        Gets the channel_secret of this IntegrationUpdate.
        LINE Channel Secret. Required for *line* integrations. 

        :return: The channel_secret of this IntegrationUpdate.
        :rtype: str
        """
        return self._channel_secret

    @channel_secret.setter
    def channel_secret(self, channel_secret):
        """
        Sets the channel_secret of this IntegrationUpdate.
        LINE Channel Secret. Required for *line* integrations. 

        :param channel_secret: The channel_secret of this IntegrationUpdate.
        :type: str
        """

        self._channel_secret = channel_secret

    @property
    def hsm_fallback_language(self):
        """
        Gets the hsm_fallback_language of this IntegrationUpdate.
        Specification of a fallback language. (Optional) Used for *WhatsApp* integrations. 

        :return: The hsm_fallback_language of this IntegrationUpdate.
        :rtype: str
        """
        return self._hsm_fallback_language

    @hsm_fallback_language.setter
    def hsm_fallback_language(self, hsm_fallback_language):
        """
        Sets the hsm_fallback_language of this IntegrationUpdate.
        Specification of a fallback language. (Optional) Used for *WhatsApp* integrations. 

        :param hsm_fallback_language: The hsm_fallback_language of this IntegrationUpdate.
        :type: str
        """

        self._hsm_fallback_language = hsm_fallback_language

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
        if not isinstance(other, IntegrationUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
