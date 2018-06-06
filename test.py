from cloudipsp import Api, Checkout, Order, Payment, Pcidss

api = Api(merchant_id=1396424, secret_key='test', request_type='xml')  # json - is default
checkout = Checkout(api=api)
order = Order(api=api)
payment = Payment(api=api)
pcidss = Pcidss(api=api)
"""""
data = {
    "preauth": 'Y',
    "currency": "RUB",
    "amount": 10000,
    "reservation_data": {
        'test': 1,
        'test2': 2
    }
}
resp = checkout.url(data)
print(resp)

order_data = {
    "order_id": "5rOqvQeysM7w1xOmRj9vnYIrAk1UH0o7",
    "amount": 10,
    "currency": "RUB"
}
order_resp = order.reverse(order_data)
print(order_resp)

payment_data = {
    "date_from": "20.04.2018 23:00:00",
    "date_to": "20.04.2018 22:00:00"
}

payment_resp = payment.reports(payment_data)
print(payment_resp)

data = {
    "currency": "RUB",
    "amount": 10000,
    "reservation_data": {
        'test': 1,
        'test2': 2
    },
    "rectoken": "d0110d00568b74b79eff1af5a1e4aedfd0c9df4e"
}
resp = payment.recurring(data)
print(resp)

data_pcidss = {
    "currency": "RUB",
    "amount": 10000,
    'card_number': "4444555566661111",
    'cvv2': "123",
    'expiry_date': "1224"
}
resp = pcidss.step_one(data_pcidss)
print(resp)

data_p2p = {
    "currency": "RUB",
    "amount": 100,
    'receiver_card_number': "4444555566661111"
}
resp = payment.p2pcredit(data_p2p)
print(resp)


data_pcidss_s_2 = {
    "md": "2956-4678A392374D3A1A",
    "pares": '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',
    'order_id': "L0y33766xyjfESCMgonf5Yj6vPGn0Vus"
}
resp = pcidss.step_two(data_pcidss_s_2)
print(resp)
"""""
data_pcidss = {
    "currency": "RUB",
    "amount": 10000,
    'card_number': "4444555511116666",
    'cvv2': "123",
    'expiry_date': "1224"
}
#resp = pcidss.step_one(data_pcidss)
print(pcidss.step_one(data_pcidss))
