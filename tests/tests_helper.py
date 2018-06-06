import os
import json

from unittest import TestCase
from cloudipsp import Api, Pcidss


class TestCase(TestCase):
    def get_api(self):
        self.data = self.get_dummy_data()
        return Api(merchant_id=self.data['merchant']['id'], secret_key=self.data['merchant']['secret'])

    def get_dummy_data(self):
        dummy_data = os.path.join(os.path.dirname(__file__), 'data', 'test_data.json')
        with open(dummy_data) as f:
            self.data = json.load(f)
        return self.data

    def create_order(self):
        pcidss = Pcidss(api=self.get_api())
        params = {
            "preauth": "Y",
            "required_rectoken": "Y"
        }
        params.update(self.data['payment_pcidss_non3ds'])
        return pcidss.step_one(params)
