
class Url(object):

    def __init__(self, baseurl, querydelimiter="&"):
        self.urltrack = baseurl
        self.pagetrack = ""
        self.querytrack = []
        self.querydelimiter = querydelimiter
        self.fragmenttrack = ""

    def __repr__(self):
        return "<url:{url}>".format(url=str(self))

    def __str__(self):
        return self.urltrack + self.pagetrack + self._query_gen() + self.fragmenttrack

    def _append(self, text):
        self.urltrack = self.urltrack + text

    def _page(self, text):
        self.pagetrack = self.pagetrack + text

    def _query_gen(self):
        if not bool(self.querytrack):
            return ""
        track = "?{name}={val}".format(
            name=list(self.querytrack[0].keys())[0],
            val=self.querytrack[0][list(self.querytrack[0].keys())[0]]
        )
        if len(self.querytrack) > 1:
            for x in self.querytrack[1:]:
                track += "{delimiter}{name}={val}".format(
                    delimiter=self.querydelimiter,
                    name=list(x.keys())[0],
                    val=x[list(x.keys())[0]]
                )
        return track

    def page(self, *args):
        """
        Accepts args. Adds page to Url
        """
        for arg in args:
            self._page("/{name}".format(name=arg))
        return self

    def query(self, **kwargs):
        for arg in list(kwargs.keys()):
            self.querytrack.append({arg: kwargs.get(arg)})
        return self

    def fragment(self, fragment):
        self.fragmenttrack = "#" + fragment
        return self
