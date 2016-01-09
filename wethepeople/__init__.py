from core import RequestObject

try:
    import objects, url
except ImportError:
    from . import objects, url



class Api(object):

    def __init__(self, apikey=None):
        """Creates Api Instance"""

        self.r = core.RequestObject
        self.apikey = apikey


    def request(self, api, value=None, shard=None,
                user_agent=None, auto_load=True,
                version=__apiversion__):


        useragent = self.user_agent if not user_agent else user_agent
        req = copy.copy(
            self._call(api, value, shard, useragent, auto_load, version))
        req.api_instance.session = self.nsobj.api_instance.session
        return req

    def req_auth(self, value=None, checksum=None, shard=None,
                 user_agent=None, auto_load=True,
                 version=__apiversion__, token=None):
        """
        Auth Requests
        :param api: The api being requested
        :param value: The value of the api
        :param shard: Shards to be requested
        :param user_agent: user_agent to be used for this request
        :param auto_load: If true the Nationstates instance will request the api on creation
        :param version: version to use.
        :param checksum: The Checksum for auth
        :param token: Token for auth
        """
        if not isinstance(checksum, str):
            raise exceptions.NSError("checksum must be type(str)")
        if not isinstance(token, str) != (token is None):
            raise exceptions.NSError("token must be type(str) or type(None)")
        useragent = self.user_agent if not user_agent else user_agent
        req = copy.copy(
            AuthNationstates("nation", value, shard, useragent, auto_load, version, checksum, token))
        req.api_instance.session = self.nsobj.api_instance.session
        return req