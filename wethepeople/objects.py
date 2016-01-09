class WTPBaseObject(object):
    pass

class WTPResultObject(WTPBaseObject):

    def _populate(self, **kwargs):

        for args in kwargs.items():
            setattr(self, args[0], args[1])
        return self


class APIResponse(WTPBaseObject):
    """
    This the response object()
    """

    def __init__(self, metadata, results):
        self._metadata = metadata
        self._results = results

    @property
    def metadata(self):
        return self._metadata

    @property
    def results(self):
        return self._results

class PetitionResponse(APIResponse):

    def ids(self):
        """
        Get the list of Petition ids
        """
        raise NotImplementedError


class Metadata(WTPResultObject):

    def __init__(self, responseinfo, requestinfo, resultset):
        self.responseinfo = responseinfo
        self.requestinfo = requestinfo
        self.resultset = resultset


class ResponseInfo(WTPResultObject):
    pass


class RequestInfo(WTPResultObject):
    pass


class ResultSet(WTPResultObject):
    pass


class Petition(WTPResultObject):
    pass

