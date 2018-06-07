from __future__ import absolute_import, unicode_literals
from cloudipsp.resources import Resource

import cloudipsp.helpers as helper


class Checkout(Resource):
    def url(self, data):
        """
        Method to generate checkout url
        :param data: order data
        :return: api response
        """
        path = '/checkout/url/'
        params = self._required(data)
        result = self.api.post(path, data=params, headers=self.__headers__)

        return self.response(result)

    def token(self, data):
        """
        Method to generate checkout token
        :param data: order data
        :return: api response
        """
        path = '/checkout/token/'
        params = self._required(data)
        result = self.api.post(path, data=params, headers=self.__headers__)

        return self.response(result)

    def verification(self, data):
        """
        Method to generate checkout verification url
        :param data: order data
        :return: api response
        """
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
        Method to generate checkout url with calendar
        :param data: order data
        :return: api response
        """
        path = '/checkout/url/'
        subscription_data = {
            're'
        }
        params = self._required(data)
        result = self.api.post(path, data=params, headers=self.__headers__)

        return self.response(result)

    @staticmethod
    def _required(data):
        """
        Required data to send
        :param data:
        :return: parameters to send
        """
        order_id = data.get('order_id') or helper.generate_order_id()
        order_desc = data.get('order_desc') or helper.get_order_desc(order_id)
        params = {
            'order_id': order_id,
            'order_desc': order_desc,
            'amount': data.get('amount', ''),
            'currency': data.get('currency', '')
        }
        helper.validate_data(params)
        params.update(data)

        return params
