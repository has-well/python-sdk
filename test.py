from cloudipsp import Api, Checkout


api = Api(merchant_id=1396424, secret_key='test', reques_type='xml')  # json - is default
checkout = Checkout(api=api)

data = {
    "currency": "USD",
    "amount": "125",
    "reservation_data": {
        'test': 1,
        'test2': 2
    }
}

print(checkout.url(data))
