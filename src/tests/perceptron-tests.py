
import unittest
import perceptron


class NeuronTests(unittest.TestCase):


    def setUp(self):
        self.sut = perceptron.Neuron([0,1,1])


    def tearDown(self):
        pass


    def test_should_has_as_many_inputs_as_the_initial_vector_passed(self):
        sut = self.sut
        self.assertEqual(3, len(sut.weights), "")
    def test_neuron_should_accept_learing_vector(self):
        sut = self.sut
        sut.learn(((0,1), 1))
    def test_neuron_should_not_change_its_input_weights_if_the_answer_is_right(self):
        sut = self.sut
        sut.learn(((0,1), 1))
        self.assertEqual([0,1,1], sut.weights)
    def test_neuron_should_change_its_input_weights_if_the_answer_is_incorrect(self):
        sut = self.sut
        sut.learn(((-1,0), 1))
        self.assertNotEqual([0,1,1], sut.weights, "If current neuron's answer is wrong it should correct its weights")
    def test_neuron_should_answer_correctly_according_to_its_weights(self):
        sut = self.sut
        self.assertEqual(1,sut.answer((0,1)), "This should be recognized as the first class")
    def test_single_neuron_recognizes_two_abstract_classes(self):
        sut = self.sut
        self.assertEqual(-1, sut.answer((-1,0)), "This should be recognized as the second class" )
    def test_neuron_should_use_activation_function(self):
        sut = self.sut
        self.assertEqual(-1, sut.answer((-3,0)), "This should be recognized as the second class")
    def test_neuron_should_use_activation_function_checking_first_class(self):
        sut = self.sut
        self.assertEqual(1, sut.answer((3,0)), "This should be recognized as the first class")
    def test_neuron_should_be_able_to_easily_work_with_floats(self):
        sut = self.sut
        self.assertEqual(1, sut.answer((3.1,0)), "This should be recognized as the first_class")
    def test_neuron_should_learn_from_epoch(self):
        sut = self.sut
        neuron = perceptron.Neuron([0,1,1])
        neuron.learn(((-1,0),1))
        sut.epoch_learn(
          (
            ((-1,0), 1),
            ((-1,0), 1)
          )
        )
        self.assertNotEqual(sut.weights, neuron.weights, "The weights should be more corrected")
    def test_neuron_training_should_stop_if_maximum_iteration_count_is_hit(self):
        sut = self.sut
        sut.weights = [1.7,0.5,-0.3]
        sut.learn_factor = 0.6
        epoch = (
          ((-1,1),-1),                 
          ((1,1), 1),
          ((-1,-1),1),
          #((-100,-899),1),
          ((1,-1),-1)
          #((1,10),1),
          #((100,1),1)      
        )
        self.assertEqual(100, sut.train(epoch), "There's no way a single neuron will learn this problem")
    def test_neuron_trainng_should_stop_if_training_set_is_learnt(self):
        sut = self.sut
        sut.learn_factor = 0.3
        epoch = (
          ((-1,0), 1),
          ((-1.1,0), 1)                
        )
        self.assertNotEqual(100, sut.train(epoch))
    def test_neuron_should_not_correct_weight_if_delta_is_zero(self):
        sut = self.sut
        self.assertEqual(1, sut.correct_weight(1, 0, 1))
    def test_neuron_should_correct_weight_if_delta_is_not_zero(self):
        sut = self.sut
        self.assertNotEqual(1, sut.correct_weight(1, 2, 1))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()