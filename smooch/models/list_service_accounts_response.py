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


class ListServiceAccountsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, service_accounts=None, has_more=None, offset=None):
        """
        ListServiceAccountsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'service_accounts': 'list[ServiceAccount]',
            'has_more': 'bool',
            'offset': 'int'
        }

        self.attribute_map = {
            'service_accounts': 'serviceAccounts',
            'has_more': 'hasMore',
            'offset': 'offset'
        }

        self._service_accounts = None
        self._has_more = None
        self._offset = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if service_accounts is not None:
          self.service_accounts = service_accounts
        if has_more is not None:
          self.has_more = has_more
        if offset is not None:
          self.offset = offset

    @property
    def service_accounts(self):
        """
        Gets the service_accounts of this ListServiceAccountsResponse.
        The list of service accounts.

        :return: The service_accounts of this ListServiceAccountsResponse.
        :rtype: list[ServiceAccount]
        """
        return self._service_accounts

    @service_accounts.setter
    def service_accounts(self, service_accounts):
        """
        Sets the service_accounts of this ListServiceAccountsResponse.
        The list of service accounts.

        :param service_accounts: The service_accounts of this ListServiceAccountsResponse.
        :type: list[ServiceAccount]
        """

        self._service_accounts = service_accounts

    @property
    def has_more(self):
        """
        Gets the has_more of this ListServiceAccountsResponse.
        Flag indicating if there are more service accounts that are not present in the response.

        :return: The has_more of this ListServiceAccountsResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this ListServiceAccountsResponse.
        Flag indicating if there are more service accounts that are not present in the response.

        :param has_more: The has_more of this ListServiceAccountsResponse.
        :type: bool
        """

        self._has_more = has_more

    @property
    def offset(self):
        """
        Gets the offset of this ListServiceAccountsResponse.
        The number of service account records skipped in the returned list.

        :return: The offset of this ListServiceAccountsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this ListServiceAccountsResponse.
        The number of service account records skipped in the returned list.

        :param offset: The offset of this ListServiceAccountsResponse.
        :type: int
        """

        self._offset = offset

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
        if not isinstance(other, ListServiceAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
