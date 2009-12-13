
import unittest
import NeuralNetworks.perceptron
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
    def test_neuron_with_the_most_close_answer_is_the_winner(self):
        self.sut = NeuralNetworks.nnetwork.NeuralNetwork(input_size=8, output_size=6)
        self.sut.network_layer = self.simple_layer()
        neuron_index = self.sut.choose_winner([3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1])
        self.assertEquals(2, neuron_index)
        
    def simple_layer(self):
        return [
            NeuralNetworks.perceptron.Neuron([0,1,1,1,1,1,1,1,1]),
            NeuralNetworks.perceptron.Neuron([0,2,2,2,2,2,2,2,2]),
            NeuralNetworks.perceptron.Neuron([0,3,3,3,3,3,3,3,3]),
            NeuralNetworks.perceptron.Neuron([0,4,4,4,4,4,4,4,4]),
            NeuralNetworks.perceptron.Neuron([0,5,5,5,5,5,5,5,5]),
            NeuralNetworks.perceptron.Neuron([0,6,6,6,6,6,6,6,6])
        ]
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(NetworkTest)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()