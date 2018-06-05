from __future__ import absolute_import, unicode_literals
from cloudipsp import Api, exceptions
from .tests_helper import TestCase


class ApiTest(TestCase):
    def setUp(self):
        self.data = self.get_dummy_data()
        self.api = Api(merchant_id=self.data['merchant']['id'], secret_key=self.data['merchant']['secret'])

    def test_request_type(self):
        self.assertEqual(self.api.request_type, 'json')

    def test_post(self):
        with self.assertRaises(exceptions.ServiceError):
            self.api._request(self.api.api_url, method="POST", data=None, headers=None)

    def test_headers(self):
        self.assertEqual(self.api._headers().get('User-Agent'), 'Python SDK')
        self.assertEqual(self.api._headers().get('Content-Type'), 'application/json; charset=utf-8')
