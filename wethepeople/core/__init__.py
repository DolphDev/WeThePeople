from requests import Session



class SessionWrapper(object):
    """
    This Class Wraps around Request.Session
    """

    def __init__(self, apikey):
        self.session = requests.Session()
        self.apikey = apikey

    def get(self, url):
        return session.get(url)

    def post(self):
        raise NotImplementedError

class RequestObject(object):
    """
    This class wraps around SessionWrapper
    """

    def __init__(self, apikey):
        self.session = SessionWrapper(apikey=apikey)

    def get(self, url):
        return self.session.get(url)

    def post(self, url):
        raise NotImplementedError



