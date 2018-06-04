from __future__ import absolute_import, unicode_literals

import re
import json
import base64
import six.moves.urllib as urllib
import xml.etree.cElementTree as ElementTree


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


def from_json(json_string):
    return json.loads(json_string)


def from_form(form_string):
    return dict(urllib.parse.parse_qsl(form_string))


def from_xml(xml):
    element = ElementTree.fromstring(xml)
    return _xml_to_dict(element.tag, _parse(element), element.attrib)


def _parse(node):
    tree = {}
    for child in node.getchildren():
        ctag = child.tag
        cattr = child.attrib
        ctext = child.text.strip().encode('utf-8') if child.text is not None else ''
        ctree = _parse(child)

        if not ctree:
            cdict = _xml_to_dict(ctag, ctext, cattr)
        else:
            cdict = _xml_to_dict(ctag, ctree, cattr)
        if ctag not in tree:
            tree.update(cdict)
            continue
        atag = '@' + ctag
        atree = tree[ctag]
        if not isinstance(atree, list):
            if not isinstance(atree, dict):
                atree = {}
            if atag in tree:
                atree['#' + ctag] = tree[atag]
                del tree[atag]
            tree[ctag] = [atree]

        if cattr:
            ctree['#' + ctag] = cattr

        tree[ctag].append(ctree)
    return tree


def _xml_to_dict(tag, value, attr=None):
    ret = {tag: value}
    if attr:
        atag = '@' + tag
        aattr = {}
        for k, v in attr.items():
            aattr[k] = v
        ret[atag] = aattr
        del atag
        del aattr
    return ret
