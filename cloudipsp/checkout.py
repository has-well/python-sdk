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
        if self.api.api_protocol != '2.0':
            raise Exception('This method allowed only for v2.0')
        path = '/checkout/url/'
        recurring_data = data.get('recurring_data', '')
        subscription_data = {
            'recurring_data': {
                'start_time': recurring_data.get('start_time', ''),
                'amount': recurring_data.get('amount', ''),
                'every': recurring_data.get('every', ''),
                'period': recurring_data.get('period', '')
            }
        }

        helper.validate_data(subscription_data['recurring_data'])
        subscription_data.update(data)
        params = self._required(subscription_data)
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
