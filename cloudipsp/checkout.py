from __future__ import absolute_import, unicode_literals
from cloudipsp.resources import Resource

import cloudipsp.helpers as helper


class Checkout(Resource):
    def url(self, data):
        params = self._required(data)
        path = "/checkout/url/"
        response = self.api.post(path, data=params, headers=self.__headers__)
        return response

    def token(self, data):
        params = self._required(data)
        path = "/checkout/token/"
        response = self.api.post(path, data=params, headers=self.__headers__)
        return response

    def _required(self, data):
        params = {
            'order_id': data.get('order_id') or helper.generate_order_id(),
            'order_desc': data.get('order_desc') or helper.generate_order_desc(),
            'amount': data.get('amount', ''),
            'currency': data.get('merchant_id', '')
        }
        params.update(data)
        return params
