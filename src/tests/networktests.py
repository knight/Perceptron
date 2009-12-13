
import unittest


class NetworkTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testTheTruth(self):
        self.assertTrue(True)
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(NetworkTest)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()