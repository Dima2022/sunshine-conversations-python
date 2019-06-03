# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DeploymentApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def activate_phone_number(self, deployment_id, deployment_activate_phone_number_body, **kwargs):
        """
        Activate a phone number on the specified deployment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.activate_phone_number(deployment_id, deployment_activate_phone_number_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Identifies the deployment. (required)
        :param DeploymentActivatePhoneNumber deployment_activate_phone_number_body: Body for an activatePhoneNumber request.  (required)
        :return: DeploymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.activate_phone_number_with_http_info(deployment_id, deployment_activate_phone_number_body, **kwargs)
        else:
            (data) = self.activate_phone_number_with_http_info(deployment_id, deployment_activate_phone_number_body, **kwargs)
            return data

    def activate_phone_number_with_http_info(self, deployment_id, deployment_activate_phone_number_body, **kwargs):
        """
        Activate a phone number on the specified deployment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.activate_phone_number_with_http_info(deployment_id, deployment_activate_phone_number_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Identifies the deployment. (required)
        :param DeploymentActivatePhoneNumber deployment_activate_phone_number_body: Body for an activatePhoneNumber request.  (required)
        :return: DeploymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['deployment_id', 'deployment_activate_phone_number_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_phone_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'deployment_id' is set
        if ('deployment_id' not in params) or (params['deployment_id'] is None):
            raise ValueError("Missing the required parameter `deployment_id` when calling `activate_phone_number`")
        # verify the required parameter 'deployment_activate_phone_number_body' is set
        if ('deployment_activate_phone_number_body' not in params) or (params['deployment_activate_phone_number_body'] is None):
            raise ValueError("Missing the required parameter `deployment_activate_phone_number_body` when calling `activate_phone_number`")


        collection_formats = {}

        path_params = {}
        if 'deployment_id' in params:
            path_params['deploymentId'] = params['deployment_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'deployment_activate_phone_number_body' in params:
            body_params = params['deployment_activate_phone_number_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/whatsapp/deployments/{deploymentId}/activate', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeploymentResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def confirm_code(self, deployment_id, deployment_confirm_code, **kwargs):
        """
        Confirm code to complete phone number activation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.confirm_code(deployment_id, deployment_confirm_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Identifies the deployment. (required)
        :param DeploymentConfirmCode deployment_confirm_code: Body for a confirmCode request.  (required)
        :return: DeploymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.confirm_code_with_http_info(deployment_id, deployment_confirm_code, **kwargs)
        else:
            (data) = self.confirm_code_with_http_info(deployment_id, deployment_confirm_code, **kwargs)
            return data

    def confirm_code_with_http_info(self, deployment_id, deployment_confirm_code, **kwargs):
        """
        Confirm code to complete phone number activation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.confirm_code_with_http_info(deployment_id, deployment_confirm_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Identifies the deployment. (required)
        :param DeploymentConfirmCode deployment_confirm_code: Body for a confirmCode request.  (required)
        :return: DeploymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['deployment_id', 'deployment_confirm_code']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method confirm_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'deployment_id' is set
        if ('deployment_id' not in params) or (params['deployment_id'] is None):
            raise ValueError("Missing the required parameter `deployment_id` when calling `confirm_code`")
        # verify the required parameter 'deployment_confirm_code' is set
        if ('deployment_confirm_code' not in params) or (params['deployment_confirm_code'] is None):
            raise ValueError("Missing the required parameter `deployment_confirm_code` when calling `confirm_code`")


        collection_formats = {}

        path_params = {}
        if 'deployment_id' in params:
            path_params['deploymentId'] = params['deployment_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'deployment_confirm_code' in params:
            body_params = params['deployment_confirm_code']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/whatsapp/deployments/{deploymentId}/code/confirm', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeploymentResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_deployment(self, deployment_create_body, **kwargs):
        """
        Create a WhatsApp deployment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_deployment(deployment_create_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeploymentCreate deployment_create_body: Body for a createDeployment request.  (required)
        :return: DeploymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_deployment_with_http_info(deployment_create_body, **kwargs)
        else:
            (data) = self.create_deployment_with_http_info(deployment_create_body, **kwargs)
            return data

    def create_deployment_with_http_info(self, deployment_create_body, **kwargs):
        """
        Create a WhatsApp deployment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_deployment_with_http_info(deployment_create_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeploymentCreate deployment_create_body: Body for a createDeployment request.  (required)
        :return: DeploymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['deployment_create_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_deployment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'deployment_create_body' is set
        if ('deployment_create_body' not in params) or (params['deployment_create_body'] is None):
            raise ValueError("Missing the required parameter `deployment_create_body` when calling `create_deployment`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'deployment_create_body' in params:
            body_params = params['deployment_create_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/whatsapp/deployments', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeploymentResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_deployment(self, deployment_id, **kwargs):
        """
        Delete the specified deployment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_deployment(deployment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Identifies the deployment. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_deployment_with_http_info(deployment_id, **kwargs)
        else:
            (data) = self.delete_deployment_with_http_info(deployment_id, **kwargs)
            return data

    def delete_deployment_with_http_info(self, deployment_id, **kwargs):
        """
        Delete the specified deployment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_deployment_with_http_info(deployment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Identifies the deployment. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['deployment_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_deployment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'deployment_id' is set
        if ('deployment_id' not in params) or (params['deployment_id'] is None):
            raise ValueError("Missing the required parameter `deployment_id` when calling `delete_deployment`")


        collection_formats = {}

        path_params = {}
        if 'deployment_id' in params:
            path_params['deploymentId'] = params['deployment_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/whatsapp/deployments/{deploymentId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_deployment(self, deployment_id, **kwargs):
        """
        Get the specified deployment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_deployment(deployment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Identifies the deployment. (required)
        :return: DeploymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_deployment_with_http_info(deployment_id, **kwargs)
        else:
            (data) = self.get_deployment_with_http_info(deployment_id, **kwargs)
            return data

    def get_deployment_with_http_info(self, deployment_id, **kwargs):
        """
        Get the specified deployment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_deployment_with_http_info(deployment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Identifies the deployment. (required)
        :return: DeploymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['deployment_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_deployment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'deployment_id' is set
        if ('deployment_id' not in params) or (params['deployment_id'] is None):
            raise ValueError("Missing the required parameter `deployment_id` when calling `get_deployment`")


        collection_formats = {}

        path_params = {}
        if 'deployment_id' in params:
            path_params['deploymentId'] = params['deployment_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/whatsapp/deployments/{deploymentId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeploymentResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_deployments(self, **kwargs):
        """
        List owned WhatsApp deployments.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_deployments(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ListDeploymentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_deployments_with_http_info(**kwargs)
        else:
            (data) = self.list_deployments_with_http_info(**kwargs)
            return data

    def list_deployments_with_http_info(self, **kwargs):
        """
        List owned WhatsApp deployments.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_deployments_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ListDeploymentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_deployments" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/whatsapp/deployments', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListDeploymentsResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
