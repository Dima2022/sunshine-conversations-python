# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Enums(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, action_size=None, action_type=None, business_system_type=None, client_status=None, confirmation_type=None, conversation_activity_type=None, deployment_activation_method=None, deployment_hosting=None, deployment_status=None, image_aspect_ratio=None, integration_status=None, integration_type=None, menu_item_type=None, message_item_size=None, message_type=None, field_type=None, quoted_message_type=None, role=None, webhook_triggers=None):
        """
        Enums - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action_size': 'str',
            'action_type': 'str',
            'business_system_type': 'str',
            'client_status': 'str',
            'confirmation_type': 'str',
            'conversation_activity_type': 'str',
            'deployment_activation_method': 'str',
            'deployment_hosting': 'str',
            'deployment_status': 'str',
            'image_aspect_ratio': 'str',
            'integration_status': 'str',
            'integration_type': 'str',
            'menu_item_type': 'str',
            'message_item_size': 'str',
            'message_type': 'str',
            'field_type': 'str',
            'quoted_message_type': 'str',
            'role': 'str',
            'webhook_triggers': 'str'
        }

        self.attribute_map = {
            'action_size': 'ActionSize',
            'action_type': 'ActionType',
            'business_system_type': 'BusinessSystemType',
            'client_status': 'ClientStatus',
            'confirmation_type': 'ConfirmationType',
            'conversation_activity_type': 'ConversationActivityType',
            'deployment_activation_method': 'DeploymentActivationMethod',
            'deployment_hosting': 'DeploymentHosting',
            'deployment_status': 'DeploymentStatus',
            'image_aspect_ratio': 'ImageAspectRatio',
            'integration_status': 'IntegrationStatus',
            'integration_type': 'IntegrationType',
            'menu_item_type': 'MenuItemType',
            'message_item_size': 'MessageItemSize',
            'message_type': 'MessageType',
            'field_type': 'FieldType',
            'quoted_message_type': 'QuotedMessageType',
            'role': 'Role',
            'webhook_triggers': 'WebhookTriggers'
        }

        self._action_size = None
        self._action_type = None
        self._business_system_type = None
        self._client_status = None
        self._confirmation_type = None
        self._conversation_activity_type = None
        self._deployment_activation_method = None
        self._deployment_hosting = None
        self._deployment_status = None
        self._image_aspect_ratio = None
        self._integration_status = None
        self._integration_type = None
        self._menu_item_type = None
        self._message_item_size = None
        self._message_type = None
        self._field_type = None
        self._quoted_message_type = None
        self._role = None
        self._webhook_triggers = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if action_size is not None:
          self.action_size = action_size
        if action_type is not None:
          self.action_type = action_type
        if business_system_type is not None:
          self.business_system_type = business_system_type
        if client_status is not None:
          self.client_status = client_status
        if confirmation_type is not None:
          self.confirmation_type = confirmation_type
        if conversation_activity_type is not None:
          self.conversation_activity_type = conversation_activity_type
        if deployment_activation_method is not None:
          self.deployment_activation_method = deployment_activation_method
        if deployment_hosting is not None:
          self.deployment_hosting = deployment_hosting
        if deployment_status is not None:
          self.deployment_status = deployment_status
        if image_aspect_ratio is not None:
          self.image_aspect_ratio = image_aspect_ratio
        if integration_status is not None:
          self.integration_status = integration_status
        if integration_type is not None:
          self.integration_type = integration_type
        if menu_item_type is not None:
          self.menu_item_type = menu_item_type
        if message_item_size is not None:
          self.message_item_size = message_item_size
        if message_type is not None:
          self.message_type = message_type
        if field_type is not None:
          self.field_type = field_type
        if quoted_message_type is not None:
          self.quoted_message_type = quoted_message_type
        if role is not None:
          self.role = role
        if webhook_triggers is not None:
          self.webhook_triggers = webhook_triggers

    @property
    def action_size(self):
        """
        Gets the action_size of this Enums.

        :return: The action_size of this Enums.
        :rtype: str
        """
        return self._action_size

    @action_size.setter
    def action_size(self, action_size):
        """
        Sets the action_size of this Enums.

        :param action_size: The action_size of this Enums.
        :type: str
        """
        allowed_values = ["compact", "full", "tall"]
        if action_size not in allowed_values:
            raise ValueError(
                "Invalid value for `action_size` ({0}), must be one of {1}"
                .format(action_size, allowed_values)
            )

        self._action_size = action_size

    @property
    def action_type(self):
        """
        Gets the action_type of this Enums.

        :return: The action_type of this Enums.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this Enums.

        :param action_type: The action_type of this Enums.
        :type: str
        """
        allowed_values = ["buy", "link", "locationRequest", "postback", "reply", "share", "webview"]
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def business_system_type(self):
        """
        Gets the business_system_type of this Enums.

        :return: The business_system_type of this Enums.
        :rtype: str
        """
        return self._business_system_type

    @business_system_type.setter
    def business_system_type(self, business_system_type):
        """
        Sets the business_system_type of this Enums.

        :param business_system_type: The business_system_type of this Enums.
        :type: str
        """
        allowed_values = ["helpscout", "slack", "zendesk"]
        if business_system_type not in allowed_values:
            raise ValueError(
                "Invalid value for `business_system_type` ({0}), must be one of {1}"
                .format(business_system_type, allowed_values)
            )

        self._business_system_type = business_system_type

    @property
    def client_status(self):
        """
        Gets the client_status of this Enums.

        :return: The client_status of this Enums.
        :rtype: str
        """
        return self._client_status

    @client_status.setter
    def client_status(self, client_status):
        """
        Sets the client_status of this Enums.

        :param client_status: The client_status of this Enums.
        :type: str
        """
        allowed_values = ["active", "blocked", "inactive", "pending"]
        if client_status not in allowed_values:
            raise ValueError(
                "Invalid value for `client_status` ({0}), must be one of {1}"
                .format(client_status, allowed_values)
            )

        self._client_status = client_status

    @property
    def confirmation_type(self):
        """
        Gets the confirmation_type of this Enums.

        :return: The confirmation_type of this Enums.
        :rtype: str
        """
        return self._confirmation_type

    @confirmation_type.setter
    def confirmation_type(self, confirmation_type):
        """
        Sets the confirmation_type of this Enums.

        :param confirmation_type: The confirmation_type of this Enums.
        :type: str
        """
        allowed_values = ["immediate", "userActivity", "prompt"]
        if confirmation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `confirmation_type` ({0}), must be one of {1}"
                .format(confirmation_type, allowed_values)
            )

        self._confirmation_type = confirmation_type

    @property
    def conversation_activity_type(self):
        """
        Gets the conversation_activity_type of this Enums.

        :return: The conversation_activity_type of this Enums.
        :rtype: str
        """
        return self._conversation_activity_type

    @conversation_activity_type.setter
    def conversation_activity_type(self, conversation_activity_type):
        """
        Sets the conversation_activity_type of this Enums.

        :param conversation_activity_type: The conversation_activity_type of this Enums.
        :type: str
        """
        allowed_values = ["conversation:read", "typing:start", "typing:stop"]
        if conversation_activity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `conversation_activity_type` ({0}), must be one of {1}"
                .format(conversation_activity_type, allowed_values)
            )

        self._conversation_activity_type = conversation_activity_type

    @property
    def deployment_activation_method(self):
        """
        Gets the deployment_activation_method of this Enums.

        :return: The deployment_activation_method of this Enums.
        :rtype: str
        """
        return self._deployment_activation_method

    @deployment_activation_method.setter
    def deployment_activation_method(self, deployment_activation_method):
        """
        Sets the deployment_activation_method of this Enums.

        :param deployment_activation_method: The deployment_activation_method of this Enums.
        :type: str
        """
        allowed_values = ["sms", "voice"]
        if deployment_activation_method not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_activation_method` ({0}), must be one of {1}"
                .format(deployment_activation_method, allowed_values)
            )

        self._deployment_activation_method = deployment_activation_method

    @property
    def deployment_hosting(self):
        """
        Gets the deployment_hosting of this Enums.

        :return: The deployment_hosting of this Enums.
        :rtype: str
        """
        return self._deployment_hosting

    @deployment_hosting.setter
    def deployment_hosting(self, deployment_hosting):
        """
        Sets the deployment_hosting of this Enums.

        :param deployment_hosting: The deployment_hosting of this Enums.
        :type: str
        """
        allowed_values = ["self", "smooch"]
        if deployment_hosting not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_hosting` ({0}), must be one of {1}"
                .format(deployment_hosting, allowed_values)
            )

        self._deployment_hosting = deployment_hosting

    @property
    def deployment_status(self):
        """
        Gets the deployment_status of this Enums.

        :return: The deployment_status of this Enums.
        :rtype: str
        """
        return self._deployment_status

    @deployment_status.setter
    def deployment_status(self, deployment_status):
        """
        Sets the deployment_status of this Enums.

        :param deployment_status: The deployment_status of this Enums.
        :type: str
        """
        allowed_values = ["deleting", "error", "integrated", "pending", "registered", "starting", "unregistered"]
        if deployment_status not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_status` ({0}), must be one of {1}"
                .format(deployment_status, allowed_values)
            )

        self._deployment_status = deployment_status

    @property
    def image_aspect_ratio(self):
        """
        Gets the image_aspect_ratio of this Enums.

        :return: The image_aspect_ratio of this Enums.
        :rtype: str
        """
        return self._image_aspect_ratio

    @image_aspect_ratio.setter
    def image_aspect_ratio(self, image_aspect_ratio):
        """
        Sets the image_aspect_ratio of this Enums.

        :param image_aspect_ratio: The image_aspect_ratio of this Enums.
        :type: str
        """
        allowed_values = ["horizontal", "square"]
        if image_aspect_ratio not in allowed_values:
            raise ValueError(
                "Invalid value for `image_aspect_ratio` ({0}), must be one of {1}"
                .format(image_aspect_ratio, allowed_values)
            )

        self._image_aspect_ratio = image_aspect_ratio

    @property
    def integration_status(self):
        """
        Gets the integration_status of this Enums.

        :return: The integration_status of this Enums.
        :rtype: str
        """
        return self._integration_status

    @integration_status.setter
    def integration_status(self, integration_status):
        """
        Sets the integration_status of this Enums.

        :param integration_status: The integration_status of this Enums.
        :type: str
        """
        allowed_values = ["active", "inactive", "error"]
        if integration_status not in allowed_values:
            raise ValueError(
                "Invalid value for `integration_status` ({0}), must be one of {1}"
                .format(integration_status, allowed_values)
            )

        self._integration_status = integration_status

    @property
    def integration_type(self):
        """
        Gets the integration_type of this Enums.

        :return: The integration_type of this Enums.
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """
        Sets the integration_type of this Enums.

        :param integration_type: The integration_type of this Enums.
        :type: str
        """
        allowed_values = ["android", "api", "apn", "fcm", "ios", "line", "mailgun", "messagebird", "messenger", "telegram", "twilio", "twitter", "viber", "web", "wechat", "whatsapp"]
        if integration_type not in allowed_values:
            raise ValueError(
                "Invalid value for `integration_type` ({0}), must be one of {1}"
                .format(integration_type, allowed_values)
            )

        self._integration_type = integration_type

    @property
    def menu_item_type(self):
        """
        Gets the menu_item_type of this Enums.

        :return: The menu_item_type of this Enums.
        :rtype: str
        """
        return self._menu_item_type

    @menu_item_type.setter
    def menu_item_type(self, menu_item_type):
        """
        Sets the menu_item_type of this Enums.

        :param menu_item_type: The menu_item_type of this Enums.
        :type: str
        """
        allowed_values = ["link", "postback", "submenu"]
        if menu_item_type not in allowed_values:
            raise ValueError(
                "Invalid value for `menu_item_type` ({0}), must be one of {1}"
                .format(menu_item_type, allowed_values)
            )

        self._menu_item_type = menu_item_type

    @property
    def message_item_size(self):
        """
        Gets the message_item_size of this Enums.

        :return: The message_item_size of this Enums.
        :rtype: str
        """
        return self._message_item_size

    @message_item_size.setter
    def message_item_size(self, message_item_size):
        """
        Sets the message_item_size of this Enums.

        :param message_item_size: The message_item_size of this Enums.
        :type: str
        """
        allowed_values = ["compact", "large"]
        if message_item_size not in allowed_values:
            raise ValueError(
                "Invalid value for `message_item_size` ({0}), must be one of {1}"
                .format(message_item_size, allowed_values)
            )

        self._message_item_size = message_item_size

    @property
    def message_type(self):
        """
        Gets the message_type of this Enums.

        :return: The message_type of this Enums.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """
        Sets the message_type of this Enums.

        :param message_type: The message_type of this Enums.
        :type: str
        """
        allowed_values = ["carousel", "file", "image", "list", "location", "text", "form", "formResponse"]
        if message_type not in allowed_values:
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def field_type(self):
        """
        Gets the field_type of this Enums.

        :return: The field_type of this Enums.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """
        Sets the field_type of this Enums.

        :param field_type: The field_type of this Enums.
        :type: str
        """
        allowed_values = ["text", "email", "select"]
        if field_type not in allowed_values:
            raise ValueError(
                "Invalid value for `field_type` ({0}), must be one of {1}"
                .format(field_type, allowed_values)
            )

        self._field_type = field_type

    @property
    def quoted_message_type(self):
        """
        Gets the quoted_message_type of this Enums.

        :return: The quoted_message_type of this Enums.
        :rtype: str
        """
        return self._quoted_message_type

    @quoted_message_type.setter
    def quoted_message_type(self, quoted_message_type):
        """
        Sets the quoted_message_type of this Enums.

        :param quoted_message_type: The quoted_message_type of this Enums.
        :type: str
        """
        allowed_values = ["message", "externalMessageId"]
        if quoted_message_type not in allowed_values:
            raise ValueError(
                "Invalid value for `quoted_message_type` ({0}), must be one of {1}"
                .format(quoted_message_type, allowed_values)
            )

        self._quoted_message_type = quoted_message_type

    @property
    def role(self):
        """
        Gets the role of this Enums.

        :return: The role of this Enums.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this Enums.

        :param role: The role of this Enums.
        :type: str
        """
        allowed_values = ["appMaker", "appUser"]
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def webhook_triggers(self):
        """
        Gets the webhook_triggers of this Enums.

        :return: The webhook_triggers of this Enums.
        :rtype: str
        """
        return self._webhook_triggers

    @webhook_triggers.setter
    def webhook_triggers(self, webhook_triggers):
        """
        Sets the webhook_triggers of this Enums.

        :param webhook_triggers: The webhook_triggers of this Enums.
        :type: str
        """
        allowed_values = ["appUser:delete", "client:add", "client:remove", "conversation:read", "conversation:referral", "conversation:start", "link:failure", "link:match", "link:success", "merge:appUser", "message:appMaker", "message:appUser", "message:delivery:channel", "message:delivery:failure", "message:delivery:user", "payment:success", "postback", "typing:appUser"]
        if webhook_triggers not in allowed_values:
            raise ValueError(
                "Invalid value for `webhook_triggers` ({0}), must be one of {1}"
                .format(webhook_triggers, allowed_values)
            )

        self._webhook_triggers = webhook_triggers

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
        if not isinstance(other, Enums):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
