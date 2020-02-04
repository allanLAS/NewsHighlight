import unittest
from app.models import Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Articles(134,"abc","trump visita japan", "abc.com","https://www.abc.net.au/news/image/11232934-16x9-700x394.jpg","japan to welcome trump","2019-06-23T08:31:32Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))