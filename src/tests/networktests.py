
import unittest
import NeuralNetworks.nnetwork

class NetworkTest(unittest.TestCase):


    def setUp(self):
        self.sut = NeuralNetworks.nnetwork.NeuralNetwork(input_size=8, output_size=6)


    def tearDown(self):
        pass
    def testTheTruth(self):
        self.assertTrue(True)
    def test_network_should_have_number_outputs_declared(self):
        answer_length = len(self.sut.answer([1,2,3,4,5,6,7,8]))
        self.assertEquals(6, answer_length)
    def test_all_neurons_should_have_the_same_output_values(self):
        answer = self.sut.answer([1,1, 1,1, 1,1, 1,1])
        self.assertEquals(1, len(set(answer)))
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(NetworkTest)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()