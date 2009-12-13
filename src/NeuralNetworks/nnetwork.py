from NeuralNetworks.perceptron import Neuron
class NeuralNetwork(object):
    def __init__(self, input_size, output_size):
        self.network_layer = []
        for i in range(output_size):
            inputs = [1 for x in range(input_size)]
            self.network_layer.append(Neuron(inputs))
    def answer(self, data=[]):
        return [self.network_layer[i].raw_answer(data) for i in range(len(self.network_layer))]
    def choose_winner(self, vector):
        difference = self.network_layer[0].difference(vector)
        winner  = 0
        for i in range(1,len(self.network_layer)):
            diff = self.network_layer[i].difference(vector)
            if diff < difference:
                winner = i
                difference = diff
        return winner