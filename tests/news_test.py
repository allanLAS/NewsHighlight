import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(1 ,"abc news","news from usa","abc.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))