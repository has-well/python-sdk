from __future__ import absolute_import, unicode_literals

import re
import json
import base64
import six.moves.urllib as urllib
import xml.etree.cElementTree as ElementTree


def to_base64(data):
    """
    Encoding data string base64 algorithm
    """
    return base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8')


def to_xml(data, start='<?xml version="1.0" encoding="UTF-8"?>'):
    return start + _data2xml(data)


def to_json(data):
    return json.dumps(data)


def to_form(data):
    return urllib.parse.urlencode(data)


def merge_dict(x, y):
    z = x.copy()
    z.update(y)
    return z


def join_url(url, *paths):
    """
    :param url: api url
    :param paths: endpoint
    :return: full url
    """
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url


def from_json(json_string):
    """
    :param json_string: json data string to encode
    :return: data dict
    """
    return json.loads(json_string)


def from_form(form_string):
    """
    :param form_string: form data string to encode
    :return: data dict
    """
    return dict(urllib.parse.parse_qsl(form_string))


def from_xml(xml):
    """
    :param xml: xml string to encode
    :return: data dict
    """
    element = ElementTree.fromstring(xml)
    return _xml_to_dict(element.tag, _parse(element), element.attrib)


def _data2xml(d):
    result_list = list()

    if isinstance(d, list):
        for sub_elem in d:
            result_list.append(_data2xml(sub_elem))

        return ''.join(d)

    if isinstance(d, dict):
        for tag_name, sub_obj in d.items():
            result_list.append("<%s>" % tag_name)
            result_list.append(_data2xml(sub_obj))
            result_list.append("</%s>" % tag_name)

        return ''.join(result_list)

    return "%s" % d


def _parse(node):
    tree = {}
    for child in node.getchildren():
        child_tag = child.tag
        child_attr = child.attrib
        child_text = child.text.strip().encode('utf-8') if child.text is not None else ''
        child_tree = _parse(child)

        if not child_tree:
            child_dict = _xml_to_dict(child_tag, child_text, child_attr)
        else:
            child_dict = _xml_to_dict(child_tag, child_tree, child_attr)
        if child_tag not in tree:
            tree.update(child_dict)
            continue
        atag = '@' + child_tag
        atree = tree[child_tag]
        if not isinstance(atree, list):
            if not isinstance(atree, dict):
                atree = {}
            if atag in tree:
                atree['#' + child_tag] = tree[atag]
                del tree[atag]
            tree[child_tag] = [atree]

        if child_attr:
            child_tree['#' + child_tag] = child_attr

        tree[child_tag].append(child_tree)
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
