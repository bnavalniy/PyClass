import random


class Matrix:

    def __init__(self, rows, columns):
        self.matrix = [[random.randint(0, 9) for x in range(columns)] for y in range(rows)]
        self.rows = rows
        self.columns = columns

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.matrix)

    def __add__(self, b):
        res = Matrix(self.rows, self.columns)
        res.matrix = []
        for j in range(len(self.matrix)):
            temp = []
            for k in range(len(self.matrix[j])):
                x = self.matrix[j][k] + b.matrix[j][k]
                temp.append(x)
            res.matrix.append(temp)
        return res


m_1 = Matrix(2, 3)
m_2 = Matrix(2, 3)
print(m_1)
print('')
print(m_2)
print('')
print(m_1 + m_2)
