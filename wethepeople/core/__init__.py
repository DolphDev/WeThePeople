from requests import Session



class SessionWrapper(object):
    """
    This Class Wraps around Request.Session
    """

    def __init__(self):
        self.session = Session()

    def get(self, url):
        return self.session.get(url, verify=True)

    def post(self):
        raise NotImplementedError

class RequestObject(object):
    """
    This class wraps around SessionWrapper
    """

    def __init__(self):
        self.session = SessionWrapper()

    def get(self, url):
        return self.session.get(url)

    def post(self, url):
        raise NotImplementedError



