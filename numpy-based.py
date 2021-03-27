# coding: utf-8
import numpy as np

features = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]])
labels = np.array([[1, 0, 0, 1, 1]])
labels = labels.reshape(5, 1)

np.random.seed(123)
weights = np.random.rand(3, 1)
bias = np.random.rand(1)
lr = 0.05


def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))


for epoch in range(20000):
    # feedforward
    XW = np.dot(features, weights) + bias
    output = sigmoid(XW)

    # backpropagation step 1
    error = output - labels
    print(error.sum())

    # backpropagation step 2
    dcost_dpred = error
    dpred_dz = sigmoid_der(output)

    output_delta = dcost_dpred * dpred_dz

    inputs = features.T
    weights -= lr * np.dot(inputs, output_delta)

    for num in output_delta:
        bias -= lr * num

new_value = np.array([0, 1, 0])
result = sigmoid(np.dot(new_value, weights) + bias)

print("result is {:.10f}".format(result[0]))
