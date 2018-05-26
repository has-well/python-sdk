class Resource(object):
    convert_resources = {}

    def __init__(self, Api=None):
        super(Resource, self).__setattr__('__data__', {})
        self.__dict__['api'] = Api

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
