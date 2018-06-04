from __future__ import absolute_import, unicode_literals
from cloudipsp.resources import Resource
from cloudipsp.exceptions import RequestError

import cloudipsp.helpers as helper


class Checkout(Resource):
    def url(self, data):
        params = self._required(data)
        path = '/checkout/url/'
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def token(self, data):
        params = self._required(data)
        path = '/checkout/token/'
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def verification(self, data):
        verification_data = {
            'verification': 'Y',
            'verification_type': data.get('verification_type', 'code')
        }
        data.update(verification_data)
        params = self._required(data)
        path = '/checkout/url/'
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def _required(self, data):
        order_id = data.get('order_id') or helper.generate_order_id()
        params = {
            'order_id': order_id,
            'order_desc': data.get('order_desc') or helper.generate_order_desc(order_id),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', '')
        }
        self._validate(params)
        params.update(data)
        return params

    def _validate(self, data):
        for key, value in data.items():
            if value == '' or None:
                raise RequestError(key)
