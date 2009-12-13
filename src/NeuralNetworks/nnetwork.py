from NeuralNetworks.perceptron import Neuron
class NeuralNetwork(object):
    def __init__(self, input_size, output_size):
        self.network_layer = []
        for i in range(output_size):
            inputs = [1 for x in range(input_size)]
            self.network_layer.append(Neuron(inputs))
    def answer(self, data=[]):
        answer = []
        for i in range(len(self.network_layer)):
            answer.append(self.network_layer[i].raw_answer(data))
        return answer
