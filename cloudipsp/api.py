from __future__ import absolute_import, unicode_literals
from cloudipsp.configuration import (__api_url__, __version__)

import os
import requests
import json
import cloudipsp.helpers as helper


class Api(object):
    user_agent = 'Python SDK'

    def __init__(self, **kwargs):
        self.merchant_id = kwargs.get('merchant_id', '')
        self.secret_key = kwargs.get('secret_key', '')
        if not self.merchant_id or not self.secret_key:
            self.merchant_id = os.environ.get('CLOUDIPSP_MERCHANT_ID', '')
            self.secret_key = os.environ.get('CLOUDIPSP_SECRETKEY', '')

    def _headers(self):
        return {
            'User-Agent': self.user_agent,
            'Content-Type': 'application/json',
        }

    def _request(self, url, method, data={}, headers={}):
        if 'merchant_id' not in data:
            data['merchant_id'] = self.merchant_id
        if 'signature' not in data:
            data['signature'] = helper.generate_signature(self.secret_key, data)
        response = requests.request(method, url, json={'request': data}, headers=headers)
        return self._response(response, response.content.decode('utf-8'))

    def _response(self, response, content):
        status = response.status_code

        if status in (200, 201):
            return json.loads(content)
        elif status == 401:
            raise Exception(
                '401')
        elif 500 <= status <= 599:
            raise Exception(
                'Service server error. Response code was: {}'
                    .format(status))

        raise Exception(
            'Response code not allowed: {status}'.format(status=status))

    def post(self, url, data={}, headers={}):
        return self._request(
            helper.join_url(__api_url__, url), 'POST',
            data=data,
            headers=headers or self._headers())
