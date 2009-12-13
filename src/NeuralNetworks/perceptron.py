
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
        requested = vector[1]

        current_answer = self.answer(inputs)
        if current_answer != requested:
            self.correct_weights(requested-current_answer,inputs)
    def correct_weights(self,d,inputs):
        self.weights[0] = self.correct_weight(self.weights[0], d, -1)
        for i in range(1, len(self.weights)):
            self.weights[i] = self.correct_weight(self.weights[i], d, inputs[i-1])
    def correct_weight(self, weight, delta, x):
        return (weight + self.learn_factor * delta * x)            
    def is_epoch_learnt(self, epoch):
        for i in range(0, len(epoch)):
            expected_answer, data_vector = epoch[i][1], epoch[i][0]
            if expected_answer != self.answer(data_vector):
                return False
        return True
    def answer(self, data_vector):
        x0 = -1.0 
        s = self.weights[0] * x0
        for i in range(1, len(self.weights)):
            s += self.weights[i] * data_vector[i-1]
        return self.activation(s)

    def activation(self, s):
        if s < 0:
            return -1
        else:
            return 1

