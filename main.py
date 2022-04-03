# coding: utf-8
from neural_network import NeuralNetwork

features = [[0, 1, 0], [0, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]]
labels = [[1, 0, 0, 1, 1]]

network = NeuralNetwork()
network.train(features, labels)

new_value = [[0, 0, 0]]
result = network.predict(new_value)

print("result is {:.10f}".format(result[0]))