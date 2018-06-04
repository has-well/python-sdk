from cloudipsp import Api, Checkout, Order

api = Api(merchant_id=1396424, secret_key='test', request_type='json')  # json - is default
checkout = Checkout(api=api)
order = Order(api=api)

data = {
    "preauth": 'Y',
    "currency": "RUB",
    "amount": 10000,
    "reservation_data": {
        'test': 1,
        'test2': 2
    }
}
#resp = checkout.url(data)
#print(resp)

order_data = {
    "order_id": "5rOqvQeysM7w1xOmRj9vnYIrAk1UH0o7",
    "amount": 10,
    "currency": "RUB"
}
order_resp = order.reverse(order_data)
print(order_resp)
