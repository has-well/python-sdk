from cloudipsp import Api, Checkout


api = Api(merchant_id=1000, secret_key='test', reques_type='json')  # json - is default
checkout = Checkout(api=api)

data = {
    "order_desc": "test order",
    "currency": "USD",
    "amount": "125",
    "reservation_data": {
        'test': 1,
        'test2': 2
    }
}

print(checkout.url(data))
