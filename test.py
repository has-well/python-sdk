from cloudipsp import Api, Checkout
import string
import random

api = Api(merchant_id=1000, secret_key='test', reques_type='json')  # json - is default
checkout = Checkout(api=api, headers={'test': '2222'})

data = {
    "order_id": ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]),
    "order_desc": "test order",
    "currency": "USD",
    "amount": "125",
    "reservation_data": {
        'test': 1,
        'test2': 2
    }
}

print(checkout.token(data))
