from __future__ import absolute_import, unicode_literals

from cloudipsp import utils
from cloudipsp import exceptions


class Resource(object):
    def __init__(self, api=None, headers=None):
        self.__dict__['api'] = api

        super(Resource, self).__setattr__('__data__', {})
        super(Resource, self).__setattr__('__headers__', headers or {})

    def __str__(self):
        return self.__data__.__str__()

    def __repr__(self):
        return self.__data__.__str__()

    def __getattr__(self, name):
        try:
            return self.__data__[name]
        except KeyError:
            return super(Resource, self).__getattribute__(name)

    def __setattr__(self, name, value):
        self.__data__[name] = value

    def __contains__(self, name):
        return name in self.__data__

    def response(self, response):
        try:
            result = None
            if self.api.request_type == 'json':
                result = utils.from_json(response).get('response', '')
            if self.api.request_type == 'xml':
                result = utils.from_xml(response).get('response', '')
            if self.api.request_type == 'form':
                result = utils.from_form(response)

            return self._get_result(result)
        except KeyError:
            raise ValueError('Undefined format error.')

    def _get_result(self, result):
        if 'response_status' in result and result.get('response_status') == 'failure':
            raise exceptions.ResponseError(result)
        if 'error_message' in result:
            raise exceptions.ResponseError(result)
        return result
