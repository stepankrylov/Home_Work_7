class Matrix:
    matrix_count = 0

    def __init__(self, list_matrix):
        self.m = list_matrix
        Matrix.matrix_count += 1

    def __add__(self, other):
        string = ''
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                if j != len(self.m[i]) - 1:
                    string += (' ' + str(self.m[i][j] + other.m[i][j]))
                else:
                    string += (' ' + str(self.m[i][j] + other.m[i][j]) + '\n')
        return f'Сумма матриц:\n' \
               f'{string}'

    def __str__(self):
        string = ''
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                if j != len(self.m[i]) - 1:
                    string += (' ' + str(self.m[i][j]))
                else:
                    string += (' ' + str(self.m[i][j]) + '\n')
        return f'Матрица № {Matrix.matrix_count}:\n' \
               f'{string}'


list_m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_1 = Matrix(list_m_1)
print(m_1)
list_m_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
m_2 = Matrix(list_m_2)
print(m_2)
print(m_1 + m_2)
