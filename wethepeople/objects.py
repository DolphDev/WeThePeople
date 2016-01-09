
class WTPBaseClass(object):

    def __init__(self, response, **kwargs):
        self.objectargs = kwargs
        return _populate

    def POST(self, *args, **kwargs):
        pass

    def GET(self, *args, **kwargs):
        pass

    def _populate(self):
        for args in kwargs.items():
            setattr(self, args[0], args[1])
        return self


"""

MetaData Classes

"""


class ResponseInfo(WTPBaseClass):
    pass


class RequestInfo(WTPBaseClass):
    pass


class Petition(WTPBaseClass):
    pass
