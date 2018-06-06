from __future__ import absolute_import, unicode_literals
from cloudipsp.configuration import (__api_url__)
from cloudipsp import exceptions

import os
import requests
import logging
import cloudipsp.helpers as helper
import cloudipsp.utils as utils

log = logging.getLogger(__name__)


class Api(object):
    user_agent = 'Python SDK'

    def __init__(self, **kwargs):
        """
        :param kwargs: args
        :arg merchant_id Merchant id numeric
        :arg secret_key Secret key string
        :arg request_type request type allowed json, xml, form
        """
        self.merchant_id = kwargs.get('merchant_id', '')
        self.secret_key = kwargs.get('secret_key', '')
        self.request_type = kwargs.get('request_type', 'json')
        if not self.merchant_id or not self.secret_key:
            self.merchant_id = os.environ.get('CLOUDIPSP_MERCHANT_ID', '')
            self.secret_key = os.environ.get('CLOUDIPSP_SECRETKEY', '')
        domain = kwargs.get('api_domain', 'api.fondy.eu')
        self.api_url = __api_url__.format(api_domain=domain)

    def _headers(self):
        """
        :return: request headers
        """
        return {
            'User-Agent': self.user_agent,
            'Content-Type': helper.get_request_type(self.request_type),
        }

    def _request(self, url, method, data, headers):
        """
        :param url: request url
        :param method: request method, POST default
        :param data: request data
        :param headers: request headers
        :return: api response
        """
        log.debug('Request Type: ' + self.request_type)
        log.debug('URL: ' + url)
        log.debug('Data: ' + str(data))
        log.debug('Headers: ' + str(headers))

        response = requests.request(method, url, data=data, headers=headers)
        return self._response(response, response.content.decode('utf-8'))

    def _response(self, response, content):
        """
        :param response: api response
        :param content: api response body
        :return: if response header 200 or 201 return response data
        """
        status = response.status_code

        log.debug('Status: ' + str(status))
        log.debug('Content: ' + content)

        if status in (200, 201):
            return content

        raise exceptions.ServiceError(
            'Response code is: {status}'.format(status=status))

    def post(self, url, data=list, headers=None):
        """
        :param url: endpoint api url
        :param data: request data
        :param headers: request headers
        :return: request
        """
        if 'merchant_id' not in data:
            data['merchant_id'] = self.merchant_id
        if 'reservation_data' in data:
            data['reservation_data'] = utils.to_b64(data['reservation_data'])
        if 'signature' not in data:
            data['signature'] = helper.get_signature(self.secret_key, data)
        data_string = helper.get_data({'request': data}, self.request_type)

        return self._request(
            utils.join_url(self.api_url, url), 'POST',
            data=data_string,
            headers=utils.merge_dict(headers, self._headers()))
