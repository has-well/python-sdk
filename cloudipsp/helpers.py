from __future__ import absolute_import, unicode_literals
from hashlib import sha1
from cloudipsp.configuration import __sign_sep__ as sep

import cloudipsp.utils as utils
import string
import random


def get_data(data, type):
    if type == 'json':
        return utils.to_json(data)
    if type == 'xml':
        return utils.to_xml(data)
    if type == 'form':
        return utils.to_form(data.get('request'))


def get_request_type(type):
    types = {
        'json': 'application/json; charset=utf-8',
        'xml': 'application/xml; charset=utf-8',
        'form': 'application/x-www-form-urlencoded; charset=utf-8'
    }
    return types.get(type, types['json'])


def generate_signature(secret_key, params):
    data = [secret_key]
    data.extend([str(params[key]) for key in sorted(iter(params.keys()))
                 if params[key] != '' and not params[key] is None])
    return sha1(sep.join(data).encode('utf-8')).hexdigest()


def generate_order_desc(order_id):
    return 'Pay for order #: ' + order_id


def generate_order_id():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
