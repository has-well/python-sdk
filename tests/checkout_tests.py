from __future__ import absolute_import, unicode_literals
from cloudipsp import Api, Checkout
from .tests_helper import TestCase


class CheckoutTest(TestCase):
    def setUp(self):
        self.data = self.get_dummy_data()
        self.api = Api(merchant_id=self.data['merchant']['id'], secret_key=self.data['merchant']['secret'])

    def test_create_url_json(self):
        checkout = Checkout(api=self.api)
        response = checkout.url(self.data.get('checkout_data'))
        self.assertEqual(response.get('response_status'), 'success')
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/json; charset=utf-8')
        self.assertIn('checkout_url', response)
        self.assertEqual(len(response.get('checkout_url')) > 0, True)

    def test_create_url_xml(self):
        self.api.request_type = 'xml'
        checkout = Checkout(api=self.api)
        response = checkout.url(self.data.get('checkout_data'))
        self.assertEqual(response.get('response_status'), 'success')
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/xml; charset=utf-8')
        self.assertIn('checkout_url', response)
        self.assertEqual(len(response.get('checkout_url')) > 0, True)

    def test_create_url_form(self):
        self.api.request_type = 'form'
        checkout = Checkout(api=self.api)
        response = checkout.url(self.data.get('checkout_data'))
        self.assertEqual(response.get('response_status'), 'success')
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/x-www-form-urlencoded; charset=utf-8')
        self.assertIn('checkout_url', response)
        self.assertEqual(len(response.get('checkout_url')) > 0, True)
