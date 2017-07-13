# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 1.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppUserUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, given_name=None, surname=None, email=None, signed_up_at=None, properties=None):
        """
        AppUserUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'given_name': 'str',
            'surname': 'str',
            'email': 'str',
            'signed_up_at': 'str',
            'properties': 'object'
        }

        self.attribute_map = {
            'given_name': 'givenName',
            'surname': 'surname',
            'email': 'email',
            'signed_up_at': 'signedUpAt',
            'properties': 'properties'
        }

        self._given_name = None
        self._surname = None
        self._email = None
        self._signed_up_at = None
        self._properties = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if given_name is not None:
          self.given_name = given_name
        if surname is not None:
          self.surname = surname
        if email is not None:
          self.email = email
        if signed_up_at is not None:
          self.signed_up_at = signed_up_at
        if properties is not None:
          self.properties = properties

    @property
    def given_name(self):
        """
        Gets the given_name of this AppUserUpdate.
        The app user's given name.

        :return: The given_name of this AppUserUpdate.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """
        Sets the given_name of this AppUserUpdate.
        The app user's given name.

        :param given_name: The given_name of this AppUserUpdate.
        :type: str
        """

        self._given_name = given_name

    @property
    def surname(self):
        """
        Gets the surname of this AppUserUpdate.
        The app user's surname.

        :return: The surname of this AppUserUpdate.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """
        Sets the surname of this AppUserUpdate.
        The app user's surname.

        :param surname: The surname of this AppUserUpdate.
        :type: str
        """

        self._surname = surname

    @property
    def email(self):
        """
        Gets the email of this AppUserUpdate.
        The app user's email.

        :return: The email of this AppUserUpdate.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AppUserUpdate.
        The app user's email.

        :param email: The email of this AppUserUpdate.
        :type: str
        """

        self._email = email

    @property
    def signed_up_at(self):
        """
        Gets the signed_up_at of this AppUserUpdate.
        A datetime string with the format *yyyy-mm-ddThh:mm:ssZ* representing the moment an appUser was created.

        :return: The signed_up_at of this AppUserUpdate.
        :rtype: str
        """
        return self._signed_up_at

    @signed_up_at.setter
    def signed_up_at(self, signed_up_at):
        """
        Sets the signed_up_at of this AppUserUpdate.
        A datetime string with the format *yyyy-mm-ddThh:mm:ssZ* representing the moment an appUser was created.

        :param signed_up_at: The signed_up_at of this AppUserUpdate.
        :type: str
        """

        self._signed_up_at = signed_up_at

    @property
    def properties(self):
        """
        Gets the properties of this AppUserUpdate.
        Custom properties for the app user.

        :return: The properties of this AppUserUpdate.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this AppUserUpdate.
        Custom properties for the app user.

        :param properties: The properties of this AppUserUpdate.
        :type: object
        """

        self._properties = properties

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
        if not isinstance(other, AppUserUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
