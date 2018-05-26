from __future__ import absolute_import, unicode_literals
from cloudipsp.resources import Resource


class Checkout(Resource):
    def url(self, data):
        path = "/checkout/url/"
        response = self.api.post(path, data)
        return response
