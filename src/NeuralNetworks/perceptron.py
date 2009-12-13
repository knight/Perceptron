
class Neuron(object):
    '''
    classdocs
    '''
    def __init__(self, initial_weights=[0,1,1]):
        '''
        Constructor
        '''
        self.weights = initial_weights
        self.learn_factor = 0.2
    def train(self, epoch, max_iter=100):
        i = 0
        while (i < max_iter) and not self.is_epoch_learnt(epoch):
            i = i + 1
            self.epoch_learn(epoch)
        return i
    def epoch_learn(self, epoch):
        for i in range(0, len(epoch)):
            self.learn(epoch[i])
    def learn(self, vector):
        inputs = vector[0]        
        requested_answer = vector[1]

        current_answer = self.answer(inputs)
        if current_answer != requested_answer:
            delta = requested_answer-current_answer
            self.correct_weights(delta,inputs)
    def adapt(self, vector):
        for i in range(1, len(self.weights)):
            self.weights[i] = self.adapted_weight_value(self.weights[i], vector[i-1])
            
    def adapted_weight_value(self, weight, input):
        return weight + self.learn_factor * (input - weight)
    def correct_weights(self,delta,inputs):
        self.weights[0] = self.correct_weight(self.weights[0], delta, -1)
        for i in range(1, len(self.weights)):
            self.weights[i] = self.correct_weight(self.weights[i], delta, inputs[i-1])
    def correct_weight(self, weight, delta, input):
        return weight + self.learn_factor * delta * input            
    def is_epoch_learnt(self, epoch):
        for i in range(0, len(epoch)):
            expected_answer, data_vector = epoch[i][1], epoch[i][0]
            if expected_answer != self.answer(data_vector):
                return False
        return True
    def answer(self, data_vector):
        return self.activation(self.raw_answer(data_vector))
    def raw_answer(self, data_vector):
        x0 = -1.0 
        s = self.weights[0] * x0
        for i in range(1, len(self.weights)):
            s += self.weights[i] * data_vector[i-1]
        return s        
    def difference(self, data_vector):
        d = 0
        for i in range(0, len(data_vector)):
            d += (data_vector[i] - self.weights[i+1])**2
        d = d**(0.5)
        return d        
    def activation(self, s):
        if s < 0:
            return -1
        else:
            return 1

