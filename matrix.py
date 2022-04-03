# coding: utf-8
class Matrix:
    height = 0
    width = 0
    data = tuple()

    def __init__(self, data):
        self.height = len(data)
        self.width = len(data[0])
        self.data = data

    @staticmethod
    def add(mat1, mat2):
        rows = []
        for i in range(len(mat1.data)):
            row = []
            for j in range(len(mat1.data[0])):
                row.append(mat1.data[i][j] + mat2.data[i][j])

            rows.append(tuple(row))

        return Matrix(tuple(rows))

    @staticmethod
    def subtract(mat1, mat2):
        rows = []
        for i in range(len(mat1.data)):
            row = []
            for j in range(len(mat1.data[0])):
                row.append(mat1.data[i][j] - mat2.data[i][j])

            rows.append(tuple(row))

        return Matrix(tuple(rows))

    @staticmethod
    def apply(mat, func):
        rows = []
        for i in range(len(mat.data)):
            row = []
            for j in range(len(mat.data[0])):
                row.append(func(mat.data[i][j]))
            rows.append(tuple(row))

        return Matrix(tuple(rows))

    @staticmethod
    def scale(mat, scalar):
        rows = []
        for i in range(len(mat.data)):
            row = []
            for j in range(len(mat.data[0])):
                row.append(mat.data[i][j] * scalar)
            rows.append(tuple(row))

        return Matrix(tuple(rows))

    @staticmethod
    def multiply(mat1, mat2):
        if mat1.width != mat2.height:
            print("The matrix dimensions don't match up!")
            return

        rows = []
        for i in range(len(mat1.data)):
            row = []
            for j in range(len(mat2.data[0])):
                entry = 0
                for k in range(len(mat2.data)):
                    entry = entry + mat1.data[i][k] * mat2.data[k][j]

                row.append(entry)

            rows.append(tuple(row))

        return Matrix(tuple(rows))

    def transpose(self):

        # rows = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
        rows = []
        for i in range(len(self.data[0])):
            row = []
            for j in range(len(self.data)):
                row.append(self.data[j][i])

            rows.append(tuple(row))

        return Matrix(tuple(rows))