from __future__ import absolute_import, unicode_literals
from cloudipsp.resources import Resource
from datetime import datetime

import cloudipsp.helpers as helper


class Pcidss(Resource):
    def step_one(self, data):
        path = '/3dsecure_step1/'
        order_id = data.get('order_id') or helper.generate_order_id()
        params = {
            'order_id': order_id,
            'order_desc': data.get('order_desc') or helper.generate_order_desc(order_id),
            'currency': data.get('currency', ''),
            'amount': data.get('amount', ''),
            'card_number': data.get('card_number', ''),
            'cvv2': data.get('cvv2', ''),
            'expiry_date': data.get('expiry_date', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def step_two(self, data):
        path = '/3dsecure_step2/'
        params = {
            'order_id': data.get('order_id', ''),
            'pares': data.get('pares', ''),
            'md': data.get('md', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)


class Payment(Resource):
    def p2pcredit(self, data):
        """
        Method P2P card credit
        :param data: date range
        :return: api response
        """
        path = '/p2pcredit/'
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

    def reports(self, data):
        """
        Method to get payment reports in date range
        :param data: date range
        :return: api response
        """
        path = '/reports/'
        params = {
            'date_from': data.get('date_from', ''),
            'date_to': data.get('date_to', '')
        }
        helper.validate_data(params)
        self._validate_reports_date(params)  # from api only one response if data invalid "General Decline"
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def recurring(self, data):
        """
        Method for recurring payment
        :param data: order data
        :return: api response
        """
        path = '/recurring/'
        order_id = data.get('order_id') or helper.generate_order_id()
        params = {
            'order_id': order_id,
            'order_desc': data.get('order_desc') or helper.generate_order_desc(order_id),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', ''),
            'rectoken': data.get('rectoken', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def _validate_reports_date(self, date):
        """
        Validating date range
        :param date: date
        """
        try:
            date_from = datetime.strptime(date['date_from'], '%d.%m.%Y %H:%M:%S')
            date_to = datetime.strptime(date['date_to'], '%d.%m.%Y %H:%M:%S')
        except ValueError:
            raise ValueError("Incorrect date format, should be 'DD.MM.YYY H:M:S'")
        if date_from > date_to:
            raise ValueError("`date_from` can't be greater than `date_to`")
