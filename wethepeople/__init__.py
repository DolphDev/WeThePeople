try:
    from objects import (Petition, Metadata,
                         ResponseInfo, RequestInfo,
                         ResultSet, PetitionResponse)

    import url
    from core import RequestObject
except ImportError:
    from . import url
    from .core import RequestObject
    from .objects import (Petition, Metadata,
                          ResponseInfo, RequestInfo,
                          ResultSet, PetitionResponse)


class Api(object):

    def __init__(self, apikey=None, apiversion="1"):
        """Creates Api Instance"""

        self.r = RequestObject()
        self.version = apiversion
        self.apikey = apikey

    @property
    def apiendpoint(self):
        return url.Url(
            "https://api.whitehouse.gov/v{v}".format(v=self.version)
        )

    def populate(self, object, response):
        return

    def get(self, pages=None, query=None):
        pages = pages if pages else list()
        query = query if query else dict()

        url = self.apiendpoint.page(*pages).query(**query)
        return self.r.get(str(url))

    def petitions(self, response):
        """
        Takes Petitions responses and creates the
        Petition Object
        """
        rjson = response.json()
        metadata = Metadata(
            ResponseInfo()._populate(**
                                    rjson["metadata"]
                                    .get("responseInfo", dict())),
            RequestInfo()._populate(**
                                   rjson["metadata"]
                                   .get("requestInfo", dict())),
            ResultSet()._populate(**
                                 rjson["metadata"]
                                 .get("resultset", dict())),
        )
        generatedlist = list()
        for petition in rjson["results"]:
            generatedlist.append(Petition()._populate(**petition))
        return PetitionResponse(metadata, generatedlist)

    def get_petitions(self, **kwargs):
        response=self.get(pages=["petitions.json"], query=kwargs)
        return self.petitions(response)

    def get_petition(self, id):
        response=self.get(pages=["petitions", str(id)+".json"], query=dict())
        return self.petitions(response)
