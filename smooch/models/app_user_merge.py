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


class AppUserMerge(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, surviving=None, discarded=None):
        """
        AppUserMerge - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'surviving': 'MergedUser',
            'discarded': 'MergedUser'
        }

        self.attribute_map = {
            'surviving': 'surviving',
            'discarded': 'discarded'
        }

        self._surviving = None
        self._discarded = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if surviving is not None:
          self.surviving = surviving
        if discarded is not None:
          self.discarded = discarded

    @property
    def surviving(self):
        """
        Gets the surviving of this AppUserMerge.
        Nested object representing the user that will survive at the end of the merge

        :return: The surviving of this AppUserMerge.
        :rtype: MergedUser
        """
        return self._surviving

    @surviving.setter
    def surviving(self, surviving):
        """
        Sets the surviving of this AppUserMerge.
        Nested object representing the user that will survive at the end of the merge

        :param surviving: The surviving of this AppUserMerge.
        :type: MergedUser
        """
        if surviving is None:
            raise ValueError("Invalid value for `surviving`, must not be `None`")

        self._surviving = surviving

    @property
    def discarded(self):
        """
        Gets the discarded of this AppUserMerge.
        Nested object representing the user to merge into the surviving user. This user will be deleted as part of the process.

        :return: The discarded of this AppUserMerge.
        :rtype: MergedUser
        """
        return self._discarded

    @discarded.setter
    def discarded(self, discarded):
        """
        Sets the discarded of this AppUserMerge.
        Nested object representing the user to merge into the surviving user. This user will be deleted as part of the process.

        :param discarded: The discarded of this AppUserMerge.
        :type: MergedUser
        """
        if discarded is None:
            raise ValueError("Invalid value for `discarded`, must not be `None`")

        self._discarded = discarded

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
        if not isinstance(other, AppUserMerge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
