from __future__ import absolute_import, unicode_literals
import re
import json
import base64
import six.moves.urllib as urllib


def data2xml(d):
    result_list = list()

    if isinstance(d, list):
        for sub_elem in d:
            result_list.append(data2xml(sub_elem))

        return ''.join(d)

    if isinstance(d, dict):
        for tag_name, sub_obj in d.items():
            result_list.append("<%s>" % tag_name)
            result_list.append(data2xml(sub_obj))
            result_list.append("</%s>" % tag_name)

        return ''.join(result_list)

    return "%s" % d


def to_base64(data):
    return base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8')


def to_xml(data, start='<?xml version="1.0" encoding="UTF-8"?>'):
    return start + data2xml(data)


def to_json(data):
    return json.dumps(data)


def to_form(data):
    return urllib.parse.urlencode(data)


def merge_dict(x, y):
    z = x.copy()
    z.update(y)
    return z


def join_url(url, *paths):
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url
