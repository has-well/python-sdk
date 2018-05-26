from __future__ import unicode_literals
from hashlib import sha1
from cloudipsp.configuration import __sign_sep__ as sep

import re
import six


def join_url(url, *paths):
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url


def generate_signature(secret_key, params):
    data = [secret_key]
    data.extend([str(params[key]) for key in sorted(iter(params.keys()))
                 if params[key] != '' and not params[key] is None])
    return sha1(sep.join(data).encode('utf-8')).hexdigest()


def merge_dict(data, *override):
    result = {}
    for current_dict in (data,) + override:
        result.update(current_dict)
    return result
