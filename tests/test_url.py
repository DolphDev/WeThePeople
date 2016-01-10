import unittest
from wethepeople import url






class url_test(unittest.TestCase):

    def test_url_is_string(self):
        test_url = url.Url("http://myurl.com")
        self.assertIsInstance(str(test_url), str)

