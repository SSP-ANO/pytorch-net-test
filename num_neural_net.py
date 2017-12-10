# Number Recognition Neural Network

# written using Anaconda3-5.0.0

import numpy 
import scipy.special

# neural network class definition
class neuralNetwork:

	# initialise the neural network
	def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
		
		# set the number of nodes in each input, hidden, output layer
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes
		
		# link weight matrices Wih Who
		# weights inside the arrays are w_i_j, withere link is from node i to node j in the next layer
		# w11 w21
		# w12 w22 etc
		self.wih = numpy.random.normal(0.0,pow(self.hnodes, -0.5), (self.hnodes,self.inodes))
		self.who = numpy.random.normal(0.0,pow(self.onodes, -0.5), (self.onodes,self.hnodes))
	
		# learning rate
		self.lr = learningrate	

		# activation function is the sigmoid function
		self.activation_function = lambda x: scipy.special.expit(x)

		pass

	# train the neural network
	def train(self, inputs_list, targets_list):

            # performing query
            final_outputs = self.query(inputs_list)

            # 2d array creation
            targets = numpy.array(targets_list, ndmin=2).T

            # output layer error is the (target - actual)
            output_errors = targets - final_outputs

            # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
            hidden_errors = numpy.dot(self.who.T, output_errors)

            # update the weights for the links between the hidden and output layers
            self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))

            # update the weights for the links between the input and hidden layers
            self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))

            pass

	# query the neural network
	def query(self, inputs_list):
		
		# converts input list to 2d array
                inputs = numpy.array(inputs_list, ndmin=2).T
                
                # calculate signals into hidden layer
                hidden_inputs = numpy.dot(self.wih, inputs)
                
                # calculate the signals emerging from hidden layer
                hidden_outputs = self.activation_function(hidden_inputs)

                # calculate signals into final output layer
                final_inputs = numpy.dot(self.who, hidden_outputs)

                # calculate the signals emerging from final output layer
                final_outputs = self.activation_function(final_inputs)

                return final_outputs

# test network configuration
input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.3

# creating an instance
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)

# test query (doesn't mean anything useful yet)
t = n.query([1.0, 0.5, -1.5])

print(t)
