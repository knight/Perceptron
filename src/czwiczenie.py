if __name__ == '__main__':
    import NeuralNetworks.perceptron
    import random
    import sys
    w0 = random.uniform(-1, 1)
    w1 = random.uniform(-1, 1)
    w2 = random.uniform(-1, 1)
    neuron = NeuralNetworks.perceptron.Neuron([w0,w1,w2])
    neuron.learn_factor = 0.45
    epoch = (
        ((0,0),     1),
        ((1,0.9),  -1),
        ((-1,-0.9), 1),
        ((2,1.9),  -1),
        ((-1,-1.1),-1),
        ((2,2.1),   1),
        ((-2,-2.1),-1),
        ((2,2.1),   1),
        ((-2,-1.9), 1),
    )
    print "Bylo ", neuron.train(epoch), " epok\r"
    print "Wyliczone wagi to ", neuron.weights, "\r"

    while True:
        print "Podaj x1:\r"
        x1 = float(sys.__stdin__.readline())
        
        print "Podaj x2:\r"
        x2 = float(sys.__stdin__.readline())
        print "Odpowiedz perceptrona to: ", neuron.answer((x1,x2))
    
    