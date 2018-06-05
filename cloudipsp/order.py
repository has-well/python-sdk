from __future__ import absolute_import, unicode_literals
from cloudipsp.resources import Resource

import cloudipsp.utils as utils
import cloudipsp.helpers as helper


class Order(Resource):
    def capture(self, data):
        path = '/capture/order_id/'
        params = {
            'order_id': data.get('order_id', ''),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def reverse(self, data):
        path = '/reverse/order_id/'
        params = {
            'order_id': data.get('order_id', ''),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def status(self, data):
        path = '/status/order_id/'
        params = {
            'order_id': data.get('order_id', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def transaction_list(self, data):
        path = '/transaction_list/'
        params = {
            'order_id': data.get('order_id', '')
        }
        helper.validate_data(params)
        params.update(data)
        self.api.request_type = 'json'  # only json allowed all other methods returns 500 error
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def atol_logs(self, data):
        path = '/get_atol_logs/'
        params = {
            'order_id': data.get('order_id', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return utils.from_json(result).get('response')
