import unittest
import wethepeople as wtp
from wethepeople.objects import PetitionResponse, SignatureResponse
from wethepeople.objects import Petition, Signature


# No requests are made for this, this just silences the ua warning


# These Tests make sure that Nationstates obj keeps concurrent all object values

class api_returns_petiton_object(unittest.TestCase):

    def test_api_petitionResponse(self):

        api = wtp.Api()
        o = api.get_petitions(mock=1)
        self.assertIsInstance(o, PetitionResponse)

    def test_api_petition(self):

        api = wtp.Api()
        o = api.get_petitions(mock=1)
        self.assertIsInstance(o.results[0], Petition)        

class api_returns_signature_object(unittest.TestCase):

    def test_api_SignatureResponse(self):

        api = wtp.Api()
        o = api.get_petitions(mock=1).results[0].search_signatures(limit=1)
        self.assertIsInstance(o, SignatureResponse)

    def test_api_petition(self):
        api = wtp.Api()
        o = api.get_petitions(mock=1).results[0].search_signatures(limit=1).results[0]
        self.assertIsInstance(o, Signature)

