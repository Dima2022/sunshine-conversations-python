# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 3.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ClientInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, app_name=None, avatar_url=None, carrier=None, city=None, country=None, device_model=None, device_platform=None, gender=None, is_payment_enabled=None, locale=None, os=None, os_version=None, phone_number=None, radio_access_technology=None, state=None, timezone=None, wifi=None):
        """
        ClientInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'app_name': 'str',
            'avatar_url': 'str',
            'carrier': 'str',
            'city': 'str',
            'country': 'str',
            'device_model': 'str',
            'device_platform': 'str',
            'gender': 'str',
            'is_payment_enabled': 'bool',
            'locale': 'str',
            'os': 'str',
            'os_version': 'str',
            'phone_number': 'str',
            'radio_access_technology': 'str',
            'state': 'str',
            'timezone': 'int',
            'wifi': 'str'
        }

        self.attribute_map = {
            'app_name': 'appName',
            'avatar_url': 'avatarUrl',
            'carrier': 'carrier',
            'city': 'city',
            'country': 'country',
            'device_model': 'deviceModel',
            'device_platform': 'devicePlatform',
            'gender': 'gender',
            'is_payment_enabled': 'isPaymentEnabled',
            'locale': 'locale',
            'os': 'os',
            'os_version': 'osVersion',
            'phone_number': 'phoneNumber',
            'radio_access_technology': 'radioAccessTechnology',
            'state': 'state',
            'timezone': 'timezone',
            'wifi': 'wifi'
        }

        self._app_name = None
        self._avatar_url = None
        self._carrier = None
        self._city = None
        self._country = None
        self._device_model = None
        self._device_platform = None
        self._gender = None
        self._is_payment_enabled = None
        self._locale = None
        self._os = None
        self._os_version = None
        self._phone_number = None
        self._radio_access_technology = None
        self._state = None
        self._timezone = None
        self._wifi = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if app_name is not None:
          self.app_name = app_name
        if avatar_url is not None:
          self.avatar_url = avatar_url
        if carrier is not None:
          self.carrier = carrier
        if city is not None:
          self.city = city
        if country is not None:
          self.country = country
        if device_model is not None:
          self.device_model = device_model
        if device_platform is not None:
          self.device_platform = device_platform
        if gender is not None:
          self.gender = gender
        if is_payment_enabled is not None:
          self.is_payment_enabled = is_payment_enabled
        if locale is not None:
          self.locale = locale
        if os is not None:
          self.os = os
        if os_version is not None:
          self.os_version = os_version
        if phone_number is not None:
          self.phone_number = phone_number
        if radio_access_technology is not None:
          self.radio_access_technology = radio_access_technology
        if state is not None:
          self.state = state
        if timezone is not None:
          self.timezone = timezone
        if wifi is not None:
          self.wifi = wifi

    @property
    def app_name(self):
        """
        Gets the app_name of this ClientInfo.
        Name of the app associated with the client.

        :return: The app_name of this ClientInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """
        Sets the app_name of this ClientInfo.
        Name of the app associated with the client.

        :param app_name: The app_name of this ClientInfo.
        :type: str
        """

        self._app_name = app_name

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this ClientInfo.
        The client's avatar URL.

        :return: The avatar_url of this ClientInfo.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this ClientInfo.
        The client's avatar URL.

        :param avatar_url: The avatar_url of this ClientInfo.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def carrier(self):
        """
        Gets the carrier of this ClientInfo.
        The client's carrier.

        :return: The carrier of this ClientInfo.
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """
        Sets the carrier of this ClientInfo.
        The client's carrier.

        :param carrier: The carrier of this ClientInfo.
        :type: str
        """

        self._carrier = carrier

    @property
    def city(self):
        """
        Gets the city of this ClientInfo.
        The client's city.

        :return: The city of this ClientInfo.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this ClientInfo.
        The client's city.

        :param city: The city of this ClientInfo.
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """
        Gets the country of this ClientInfo.
        The client's country.

        :return: The country of this ClientInfo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this ClientInfo.
        The client's country.

        :param country: The country of this ClientInfo.
        :type: str
        """

        self._country = country

    @property
    def device_model(self):
        """
        Gets the device_model of this ClientInfo.
        The client's device model.

        :return: The device_model of this ClientInfo.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """
        Sets the device_model of this ClientInfo.
        The client's device model.

        :param device_model: The device_model of this ClientInfo.
        :type: str
        """

        self._device_model = device_model

    @property
    def device_platform(self):
        """
        Gets the device_platform of this ClientInfo.
        The client's device platform.

        :return: The device_platform of this ClientInfo.
        :rtype: str
        """
        return self._device_platform

    @device_platform.setter
    def device_platform(self, device_platform):
        """
        Sets the device_platform of this ClientInfo.
        The client's device platform.

        :param device_platform: The device_platform of this ClientInfo.
        :type: str
        """

        self._device_platform = device_platform

    @property
    def gender(self):
        """
        Gets the gender of this ClientInfo.
        The client user's gender.

        :return: The gender of this ClientInfo.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this ClientInfo.
        The client user's gender.

        :param gender: The gender of this ClientInfo.
        :type: str
        """

        self._gender = gender

    @property
    def is_payment_enabled(self):
        """
        Gets the is_payment_enabled of this ClientInfo.
        Whether or not payment is enabled for client.

        :return: The is_payment_enabled of this ClientInfo.
        :rtype: bool
        """
        return self._is_payment_enabled

    @is_payment_enabled.setter
    def is_payment_enabled(self, is_payment_enabled):
        """
        Sets the is_payment_enabled of this ClientInfo.
        Whether or not payment is enabled for client.

        :param is_payment_enabled: The is_payment_enabled of this ClientInfo.
        :type: bool
        """

        self._is_payment_enabled = is_payment_enabled

    @property
    def locale(self):
        """
        Gets the locale of this ClientInfo.
        The client's locale.

        :return: The locale of this ClientInfo.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this ClientInfo.
        The client's locale.

        :param locale: The locale of this ClientInfo.
        :type: str
        """

        self._locale = locale

    @property
    def os(self):
        """
        Gets the os of this ClientInfo.
        The client's OS.

        :return: The os of this ClientInfo.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this ClientInfo.
        The client's OS.

        :param os: The os of this ClientInfo.
        :type: str
        """

        self._os = os

    @property
    def os_version(self):
        """
        Gets the os_version of this ClientInfo.
        The client's OS version.

        :return: The os_version of this ClientInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this ClientInfo.
        The client's OS version.

        :param os_version: The os_version of this ClientInfo.
        :type: str
        """

        self._os_version = os_version

    @property
    def phone_number(self):
        """
        Gets the phone_number of this ClientInfo.
        The client's phone number.

        :return: The phone_number of this ClientInfo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this ClientInfo.
        The client's phone number.

        :param phone_number: The phone_number of this ClientInfo.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def radio_access_technology(self):
        """
        Gets the radio_access_technology of this ClientInfo.
        The client's radioAccessTechnology (Ex. HSDPA).

        :return: The radio_access_technology of this ClientInfo.
        :rtype: str
        """
        return self._radio_access_technology

    @radio_access_technology.setter
    def radio_access_technology(self, radio_access_technology):
        """
        Sets the radio_access_technology of this ClientInfo.
        The client's radioAccessTechnology (Ex. HSDPA).

        :param radio_access_technology: The radio_access_technology of this ClientInfo.
        :type: str
        """

        self._radio_access_technology = radio_access_technology

    @property
    def state(self):
        """
        Gets the state of this ClientInfo.
        The client's state or province.

        :return: The state of this ClientInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ClientInfo.
        The client's state or province.

        :param state: The state of this ClientInfo.
        :type: str
        """

        self._state = state

    @property
    def timezone(self):
        """
        Gets the timezone of this ClientInfo.
        The client's timezone offset.

        :return: The timezone of this ClientInfo.
        :rtype: int
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ClientInfo.
        The client's timezone offset.

        :param timezone: The timezone of this ClientInfo.
        :type: int
        """

        self._timezone = timezone

    @property
    def wifi(self):
        """
        Gets the wifi of this ClientInfo.
        Whether or not the client has wifi.

        :return: The wifi of this ClientInfo.
        :rtype: str
        """
        return self._wifi

    @wifi.setter
    def wifi(self, wifi):
        """
        Sets the wifi of this ClientInfo.
        Whether or not the client has wifi.

        :param wifi: The wifi of this ClientInfo.
        :type: str
        """

        self._wifi = wifi

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
        if not isinstance(other, ClientInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
