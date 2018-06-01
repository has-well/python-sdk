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
        order_id = helper.generate_order_id()
        params = {
            'order_id': data.get('order_id') or order_id,
            'order_desc': data.get('order_desc') or helper.generate_order_desc(order_id),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', '')
        }
        params.update(data)
        return params
