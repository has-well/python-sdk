import os
import json

from unittest import TestCase


class TestCase(TestCase):
    def get_dummy_data(self):
        dummy_data = os.path.join(os.path.dirname(__file__), 'data', 'test_data.json')
        with open(dummy_data) as f:
            data = json.load(f)
        return data
