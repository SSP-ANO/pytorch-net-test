# Number Recognition Neural Network

# Anaconda3-5.0.0

import numpy 

# neural network class definition
class neuralNetwork:

	# initialise the neural network
	def _init_(self, inputnodes, hiddennodes, outputnotes, learningrate):
		
		# set the number of nodes in each input, hidden, output layer
		
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes
		
		# learning rate
		
		self.lr = learningrate
		pass

	# train the neural network
	def train():
		pass

	# query the neural network
	def query():
		pass

# test network configuration
input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.3

# creating an instance

n = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

# link weight matrices Wih Who
# weights inside the arrays are w_i_j, withere link is from node i to node j in the next layer
# w11 w21
# w12 w22 etc

self.wih = numpy.random.normal(0.0,pow(self.hnodes, -0.5), (self.hnodes,self.inodes))
self.who = numpy.random.normal(0.0,pow(self.onodes, -0.5), (self.onodes,self.hnodes))


