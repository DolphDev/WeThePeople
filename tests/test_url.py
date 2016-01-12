import unittest
from wethepeople import Url






class url_test(unittest.TestCase):

    def test_url_is_string(self):
        test_url = Url("http://myurl.com")
        self.assertIsInstance(str(test_url), str)

