# coding: utf-8
import math
import random
from matrix import Matrix


class NeuralNetwork:
    def __init__(self, lr=0.5):
        self._lr = lr
        random.seed(123)
        pass

    def activation(self, x):
        return 1/(1+math.exp(-x))

    def activation_derivative(self, x):
        return self.activation(x) * (1 - self.activation(x))

    def calc_activation(self, x):
        """
        Calc activation function
        :param list[float] x:
        :return: list[float]
        """
        return Matrix.apply(x, self.activation)
        # r = []
        # for i in range(len(x)):
        #     r.append(self.activation(x[i]))
        # return r

    def calc_activation_derivative(self, x):
        """
        Calc derivative for activation function
        :param list[float] x:
        :return: list[float]
        """
        return Matrix.apply(x, self.activation_derivative)
        # r = []
        # for i in range(len(x)):
        #     r.append(self.activation_derivative(x[i]))
        # return r

    def transpose(self, x):
        """
        Transpose x
        :param list[list[float]] x:
        :return: list[float]
        """
        return [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

    def train(self, features, labels):
        """
        Train model
        :param list[list] features:
        :param list[list] labels:
        :return: None
        """
        assert len(features) > 0, "features should not be empty array"
        assert len(labels) > 0, "labels should not be empty array"
        assert len(features[0]) > 0, "features should be 2D array"
        assert len(labels[0]) > 0, "labels should be 2D array"

        dim = features[0]
        bias = random.uniform(0, 1)
        weights = []
        for i in range(len(dim)):
            weights.append(random.uniform(0, 1))

        features_matrix = Matrix(features)
        weights_matrix = Matrix([weights]).transpose()
        bias_matrix = Matrix([[bias]*len(features)]).transpose()
        labels_matrix = Matrix(labels).transpose()

        for epoch in range(20000):
            XW = Matrix.multiply(features_matrix, weights_matrix)
            XW = Matrix.add(XW, bias_matrix)
            output = self.calc_activation(XW)

            # backpropagation step 1
            error = Matrix.subtract(output, labels_matrix)
            s = 0
            for i in error.data:
                s += i[0]
            print(s)

            # backpropagation step 2
            dcost_dpred = error
            dpred_dz = self.calc_activation_derivative(output)

            output_delta = Matrix.multiply(dcost_dpred, dpred_dz.transpose())
            inputs = features_matrix.transpose()

            weights_matrix = Matrix.scale(weights_matrix, self._lr)
            z = Matrix.multiply(inputs, output_delta)
            weights_matrix = Matrix.subtract(weights_matrix, z)

            output_delta_scaled = Matrix.scale(output_delta, self._lr)
            bias_matrix = Matrix.subtract(bias_matrix, output_delta_scaled)

        self._weights = weights_matrix
        self._bias = bias_matrix

    def predict(self, new_value):
        n = Matrix(new_value)
        r = Matrix.multiply(n, self._weights)
        r = Matrix.add(r, self._bias)
        return self.calc_activation(r).data[0]

