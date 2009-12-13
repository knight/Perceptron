import unittest
import tests


all = unittest.TestSuite([
          tests.perceptrontests.suite(),
          tests.networktests.suite()
])



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.TextTestRunner().run(all)

