from __future__ import absolute_import, unicode_literals
from cloudipsp.configuration import (__api_url__)
from cloudipsp import exceptions

import os
import requests
import cloudipsp.helpers as helper
import cloudipsp.utils as utils


class Api(object):
    user_agent = 'Python SDK'

    def __init__(self, **kwargs):
        """
        :param kwargs: 
        :arg merchant_id Merchant id numeric
        :arg secret_key Secret key string
        """
        self.merchant_id = kwargs.get('merchant_id', '')
        self.secret_key = kwargs.get('secret_key', '')
        self.request_type = kwargs.get('request_type', 'json')
        if not self.merchant_id or not self.secret_key:
            self.merchant_id = os.environ.get('CLOUDIPSP_MERCHANT_ID', '')
            self.secret_key = os.environ.get('CLOUDIPSP_SECRETKEY', '')
        self.api_url = __api_url__.format(api_domain=kwargs.get('api_domain', 'api.fondy.eu'))

    def _headers(self):
        return {
            'User-Agent': self.user_agent,
            'Content-Type': helper.get_request_type(self.request_type),
        }

    def _request(self, url, method, data, headers):
        response = requests.request(method, url, data=data, headers=headers)
        return self._response(response, response.content.decode('utf-8'))

    def _response(self, response, content):
        status = response.status_code

        if status in (200, 201):
            return content

        raise exceptions.ServerError(
            'Response code is: {status}'.format(status=status))

    def post(self, url, data=None, headers=None):
        if 'merchant_id' not in data:
            data['merchant_id'] = self.merchant_id
        if 'reservation_data' in data:
            data['reservation_data'] = utils.to_base64(data['reservation_data'])
        if 'signature' not in data:
            data['signature'] = helper.generate_signature(self.secret_key, data)
        data_string = helper.get_data({'request': data}, self.request_type)

        return self._request(
            utils.join_url(self.api_url, url), 'POST',
            data=data_string,
            headers=utils.merge_dict(headers, self._headers()))
