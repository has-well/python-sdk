from cloudipsp import Api, Checkout
import os
from multiprocessing import Process
import requests
import json

""""
def test():
    api = Api(
        merchant_id=1598278,
        # merchant_id=1598166,
        secret_key='Unvpg6dB3PilEWyPZyBrqBnqy1y5eMnd',
        # secret_key='bSFeDkH1rKepl0MmaowMNjKV5uMBAMM3',
        request_type='json',
        api_protocol='1.0',
        # api_domain='has-well.com'
        api_domain='api.dev.fondy.eu'
    )  # json - is default
    # api_domain='api.dev.fondy.eu')  # json - is default
    checkout = Checkout(api=api)
    data = {
        "currency": "UAH",
        "order_desc": "\"&lt;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&gt;&#x61;&#x6C;&#x65;&#x72;&#x74;&lpar;&#x31;&rpar;&semi;&lt;&sol;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&gt;",
        "delayed": 'Y',
        "amount": 20000,
        "response_url": '<script>alert(1);</script>',
        "lifetime": 60 * 60 * 24 * 2,
        "reservation_data": {
            "products": [
                {
                    "CODE": 1,
                    "UKTZED": 1,
                    "UNITCODE": 22,
                    "NAME": "Миндаль жар.",
                    "UNITNAME": "кг.",
                    "AMOUNT": 2,
                    "PRICE": 10.00,
                    "LETTER": 'M',
                    "COST": 20.00
                },
                {
                    "CODE": 2,
                    "UKTZED": 33,
                    "UNITCODE": 44,
                    "NAME": "Кеш жар.",
                    "UNITNAME": "кг.",
                    "AMOUNT": 3,
                    "PRICE": 10.00,
                    "LETTER": 'С',
                    "COST": 30.00
                }
            ]
        }
    }
    response = checkout.token(data)
    print(response)
    r = requests.post('https://api.dev.fondy.eu/api/checkout/ajax', json={
        "request": {"card_number": "4444555511116666", "cvv2": "232", "cardholder": "test",
                    "email": "dimoncheg12@mail.ru", "expiry_date": "0333", "payment_system": "card",
                    "token": response['token'], "kkh": "eyJpZCI6IjBiMjBiNTk4MDIzZTc5M2YxMGU4ZDYwMmNhMzhhMWQ1In0="}})
    print(r.json())
    api = Api(
        merchant_id=1598260,
        # merchant_id=1598166,
        secret_key='nBNM30ibDJNkPfPTGuog2m77zO3rPnxE',
        # secret_key='bSFeDkH1rKepl0MmaowMNjKV5uMBAMM3',
        request_type='json',
        api_protocol='1.0',
        # api_domain='has-well.com'
        api_domain='api.dev.fondy.eu'
    )  # json - is default
    # api_domain='api.dev.fondy.eu')  # json - is default
    checkout = Checkout(api=api)
    data = {
        "currency": "UAH",
        "order_desc": "\"&lt;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&gt;&#x61;&#x6C;&#x65;&#x72;&#x74;&lpar;&#x31;&rpar;&semi;&lt;&sol;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&gt;",
        "delayed": 'Y',
        "amount": 20000,
        "response_url": '<script>alert(1);</script>',
        "lifetime": 60 * 60 * 24 * 2,
        "reservation_data": {
            "products": [
                {
                    "CODE": 1,
                    "UKTZED": 1,
                    "UNITCODE": 22,
                    "NAME": "тест 2 жар.",
                    "UNITNAME": "кг.",
                    "AMOUNT": 2,
                    "PRICE": 10.00,
                    "LETTER": 'M',
                    "COST": 20.00
                },
                {
                    "CODE": 2,
                    "UKTZED": 33,
                    "UNITCODE": 44,
                    "NAME": "тест 3 жар.",
                    "UNITNAME": "кг.",
                    "AMOUNT": 3,
                    "PRICE": 10.00,
                    "LETTER": 'С',
                    "COST": 30.00
                }
            ]
        }
    }
    response = checkout.token(data)
    print(response)
    r = requests.post('https://api.dev.fondy.eu/api/checkout/ajax', json={
        "request": {"card_number": "4444555511116666", "cvv2": "232", "cardholder": "test",
                    "email": "dimoncheg12@mail.ru", "expiry_date": "0333", "payment_system": "card",
                    "token": response['token'], "kkh": "eyJpZCI6IjBiMjBiNTk4MDIzZTc5M2YxMGU4ZDYwMmNhMzhhMWQ1In0="}})
    print(r.json())

if __name__ == '__main__':
    numbers = 10
    procs = []

    for number in range(numbers):
        proc = Process(target=test)
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
"""""
api = Api(
        merchant_id=1598166,
        # merchant_id=1598166,
        secret_key='bSFeDkH1rKepl0MmaowMNjKV5uMBAMM3',
        # secret_key='bSFeDkH1rKepl0MmaowMNjKV5uMBAMM3',
        request_type='json',
        api_protocol='1.0',
        # api_domain='has-well.com'
        api_domain='has-well.com'
    )
checkout = Checkout(api=api)
data = {
        "currency": "UAH",
        "order_desc": "\"&lt;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&gt;&#x61;&#x6C;&#x65;&#x72;&#x74;&lpar;&#x31;&rpar;&semi;&lt;&sol;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&gt;",
        "delayed": 'Y',
        "amount": 20000,
        "response_url": '<script>alert(1);</script>',
        "lifetime": 60 * 60 * 24 * 2,
    }
response = checkout.token(data)
print(response)