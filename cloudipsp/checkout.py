from __future__ import absolute_import, unicode_literals
from cloudipsp.resources import Resource

import cloudipsp.helpers as helper


class Checkout(Resource):
    def url(self, data):
        path = '/checkout/url/'
        params = self._required(data)
        result = self.api.post(path, data=params, headers=self.__headers__)

        return self.response(result)

    def token(self, data):
        path = '/checkout/token/'
        params = self._required(data)
        result = self.api.post(path, data=params, headers=self.__headers__)

        return self.response(result)

    def verification(self, data):
        path = '/checkout/url/'
        verification_data = {
            'verification': 'Y',
            'verification_type': data.get('verification_type', 'code')
        }
        data.update(verification_data)
        params = self._required(data)
        result = self.api.post(path, data=params, headers=self.__headers__)

        return self.response(result)

    def subscription(self, data):
        """
        :param data: 
        :return: 
        """

    def _required(self, data):
        order_id = data.get('order_id') or helper.generate_order_id()
        params = {
            'order_id': order_id,
            'order_desc': data.get('order_desc') or helper.generate_order_desc(order_id),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', '')
        }
        helper.validate_data(params)
        params.update(data)

        return params
