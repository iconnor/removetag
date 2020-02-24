
from server import app
import unittest 

class TagTests(unittest.TestCase):

    def test_remove_tag(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200) 
