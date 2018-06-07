from __future__ import absolute_import, unicode_literals
from cloudipsp import Api, Checkout
from .tests_helper import TestCase


class CheckoutTest(TestCase):
    def setUp(self):
        self.api = self.get_api()
        self.checkout = Checkout(api=self.api)

    def test_create_url_json(self):
        response = self.checkout.url(self.data.get('checkout_data'))
        self.assertEqual(response.get('response_status'), 'success')
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/json; charset=utf-8')
        self.assertIn('checkout_url', response)
        self.assertEqual(len(response.get('checkout_url')) > 0, True)

    def test_create_url_json_v2(self):
        self.api.api_protocol = '2.0'
        response = self.checkout.url(self.data.get('checkout_data'))
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/json; charset=utf-8')
        self.assertEqual(response.get('version'), '2.0')
        self.assertEqual(len(response.get('data')) > 0, True)

    def test_create_url_xml(self):
        self.api.request_type = 'xml'
        response = self.checkout.url(self.data.get('checkout_data'))

        self.assertEqual(response.get('response_status'), 'success')
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/xml; charset=utf-8')
        self.assertIn('checkout_url', response)
        self.assertEqual(len(response.get('checkout_url')) > 0, True)

    def test_create_url_form(self):
        self.api.request_type = 'form'
        response = self.checkout.url(self.data.get('checkout_data'))

        self.assertEqual(response.get('response_status'), 'success')
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/x-www-form-urlencoded; charset=utf-8')
        self.assertIn('checkout_url', response)
        self.assertEqual(len(response.get('checkout_url')) > 0, True)

    def test_create_token(self):
        response = self.checkout.token(self.data.get('checkout_data'))
        self.assertEqual(response.get('response_status'), 'success')
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/json; charset=utf-8')
        self.assertIn('token', response)
        self.assertEqual(len(response.get('token')) > 0, True)

    def test_create_url_verify(self):
        response = self.checkout.verification(self.data.get('checkout_data'))
        self.assertEqual(response.get('response_status'), 'success')
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/json; charset=utf-8')
        self.assertIn('checkout_url', response)
        self.assertEqual(len(response.get('checkout_url')) > 0, True)
