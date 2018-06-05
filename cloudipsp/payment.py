from __future__ import absolute_import, unicode_literals
from cloudipsp.resources import Resource

import cloudipsp.helpers as helper


class Payment(Resource):
    def reports(self, data):
        path = '/reports/'
        params = {
            'date_from': data.get('date_from', ''),
            'date_to': data.get('date_to', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def recurring(self, data):
        path = '/recurring/'
        order_id = data.get('order_id') or helper.generate_order_id()
        params = {
            'order_id': order_id,
            'order_desc': data.get('order_desc') or helper.generate_order_desc(order_id),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)
