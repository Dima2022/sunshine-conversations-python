# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 3.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, settings=None, metadata=None):
        """
        AppUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'settings': 'AppSettings',
            'metadata': 'object'
        }

        self.attribute_map = {
            'name': 'name',
            'settings': 'settings',
            'metadata': 'metadata'
        }

        self._name = None
        self._settings = None
        self._metadata = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if name is not None:
          self.name = name
        if settings is not None:
          self.settings = settings
        if metadata is not None:
          self.metadata = metadata

    @property
    def name(self):
        """
        Gets the name of this AppUpdate.
        The app's name.

        :return: The name of this AppUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppUpdate.
        The app's name.

        :param name: The name of this AppUpdate.
        :type: str
        """

        self._name = name

    @property
    def settings(self):
        """
        Gets the settings of this AppUpdate.

        :return: The settings of this AppUpdate.
        :rtype: AppSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this AppUpdate.

        :param settings: The settings of this AppUpdate.
        :type: AppSettings
        """

        self._settings = settings

    @property
    def metadata(self):
        """
        Gets the metadata of this AppUpdate.
        Flat JSON object containing any custom properties associated with the app.

        :return: The metadata of this AppUpdate.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this AppUpdate.
        Flat JSON object containing any custom properties associated with the app.

        :param metadata: The metadata of this AppUpdate.
        :type: object
        """

        self._metadata = metadata

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
        if not isinstance(other, AppUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
