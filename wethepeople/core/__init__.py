from requests import Session
from time import time as timestamp
#from . import exceptions

__rltracker__ = list()



def ErrorProbe(response):
    """
    Probes the Response for errors
    """
    responsejson = response.json()["metadata"]["responseInfo"]
    if responsejson.get("status") is 400 or responsejson.get("status") is 404:
        # Yes, 400 is 404 for some reason
        # 404 In case they fix it
        raise exceptions.PetitionNotFound(
            "Error {errorCode}\nMessage: {message}".format(
                errorCode=responsejson.get("errorCode"),
                message=responsejson.get("developerMessage")
            ))
    if responsejson.get("status") is 599:
        raise exceptions.InternalServerError(
            "Error {errorCode}\nMessage: {message}".format(
                errorCode=responsejson.get("errorCode"),
                message=responsejson.get("developerMessage")
            ))


class RateLimit(object):

    """
    This object wraps around the ratelimiting system

    Classes that use the rate-limiter must inherit this.

    If a function needs to use the rate limiter, it must create
    a RateLimit() obj and use its methods. This protect the
    global state of the Rate Limiter from side effects.

    """

    @property
    def rltime(self):
        """Returns the current tracker"""
        return globals()["__rltracker__"]

    @rltime.setter
    def rltime(self, val):
        """Sets the current tracker"""
        globals()["__rltracker__"] = val

    def ratelimitcheck(self, amount_allow=9, within_time=1):
        """Checks if WeThePeople needs pause to prevent api banning"""

        if len(self.rltime) >= amount_allow:
            currenttime = timestamp()
            try:
                while (self.rltime[-1]+within_time) < currenttime:
                    del self.rltime[-1]
                if len(self.rltime) >= amount_allow:
                    return False
            except IndexError as err:
                return len(self.rltime) == 0

            else:
                return True
        else:
            return True

    def add_timestamp(self):
        """Adds timestamp to rltime"""
        self.rltime = [timestamp()] + self.rltime


class SessionWrapper(RateLimit):

    """
    This Class Wraps around Request.Session
    """

    def __init__(self):
        self.session = Session()

    def get(self, url):
        while not self.ratelimitcheck():
            time.sleep(0.1)
        response = self.session.get(url, verify=True)
        self.add_timestamp()
        print(self.rltime)
        return response

    def post(self, url, params):
        return self.session.POST(url, params=params, verify=True)


class RequestObject(object):

    """
    This class wraps around SessionWrapper
    """

    def __init__(self):
        self.session = SessionWrapper()

    def get(self, url):
        response = self.session.get(url)
        ErrorProbe(response)
        return response

    def post(self, url):
        raise NotImplementedError
