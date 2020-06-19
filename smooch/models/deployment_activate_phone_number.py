# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeploymentActivatePhoneNumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, phone_number=None, verified_name_certificate=None, method=None):
        """
        DeploymentActivatePhoneNumber - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phone_number': 'str',
            'verified_name_certificate': 'str',
            'method': 'str'
        }

        self.attribute_map = {
            'phone_number': 'phoneNumber',
            'verified_name_certificate': 'verifiedNameCertificate',
            'method': 'method'
        }

        self._phone_number = None
        self._verified_name_certificate = None
        self._method = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if phone_number is not None:
          self.phone_number = phone_number
        if verified_name_certificate is not None:
          self.verified_name_certificate = verified_name_certificate
        if method is not None:
          self.method = method

    @property
    def phone_number(self):
        """
        Gets the phone_number of this DeploymentActivatePhoneNumber.
        The phone number to send the activation code to.

        :return: The phone_number of this DeploymentActivatePhoneNumber.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this DeploymentActivatePhoneNumber.
        The phone number to send the activation code to.

        :param phone_number: The phone_number of this DeploymentActivatePhoneNumber.
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")

        self._phone_number = phone_number

    @property
    def verified_name_certificate(self):
        """
        Gets the verified_name_certificate of this DeploymentActivatePhoneNumber.
        The verified name certificate for the phone number.

        :return: The verified_name_certificate of this DeploymentActivatePhoneNumber.
        :rtype: str
        """
        return self._verified_name_certificate

    @verified_name_certificate.setter
    def verified_name_certificate(self, verified_name_certificate):
        """
        Sets the verified_name_certificate of this DeploymentActivatePhoneNumber.
        The verified name certificate for the phone number.

        :param verified_name_certificate: The verified_name_certificate of this DeploymentActivatePhoneNumber.
        :type: str
        """
        if verified_name_certificate is None:
            raise ValueError("Invalid value for `verified_name_certificate`, must not be `None`")

        self._verified_name_certificate = verified_name_certificate

    @property
    def method(self):
        """
        Gets the method of this DeploymentActivatePhoneNumber.
        The method desired to receive the activation code. See [**DeploymentActivationMethodEnum**](Enums.md#DeploymentActivationMethodEnum) for available values.

        :return: The method of this DeploymentActivatePhoneNumber.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this DeploymentActivatePhoneNumber.
        The method desired to receive the activation code. See [**DeploymentActivationMethodEnum**](Enums.md#DeploymentActivationMethodEnum) for available values.

        :param method: The method of this DeploymentActivatePhoneNumber.
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")

        self._method = method

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
        if not isinstance(other, DeploymentActivatePhoneNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
