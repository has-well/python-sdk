from cloudipsp import Api, Checkout
import string
import random

api = Api(merchant_id=1000, secret_key='test')
checkout = Checkout(Api=api)

data = {
    "order_id": ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]),
    "order_desc": "test order",
    "currency": "USD",
    "amount": "125"
}

print(checkout.url(data))
