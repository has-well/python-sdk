from __future__ import absolute_import, unicode_literals
from cloudipsp import Api, Order, exceptions
from .tests_helper import TestCase


class OrderTest(TestCase):
    def setUp(self):
        self.data = self.get_dummy_data()
        self.api = Api(merchant_id=self.data['merchant']['id'], secret_key=self.data['merchant']['secret'])
        self.order = Order(api=self.api)

    def test_get_order_status(self):
        response = self.order.status(self.data['order_data'])
        self.assertEqual(response.get('response_status'), 'success')
        self.assertIn('order_status', response)

    def test_get_order_trans_list(self):
        response = self.order.transaction_list(self.data['order_data'])
        self.assertIsInstance(response, list)
        self.assertIn('order_id', response[0])

    def test_refund(self):
        response = self.order.reverse(self.data['order_full_data'])
        self.assertEqual(response.get('response_status'), 'success')
        self.assertIn('reverse_status', response)

    # def test_atol(self):
    #    response = self.order.atol_logs(self.data['order_data'])
    #    self.assertIsInstance(response, list)

    def test_capture(self):
        with self.assertRaises(exceptions.ResponseError):
            self.order.capture(self.data['order_full_data'])
