class Cell:
    def __init__(self, param, row):
        self.p = param
        self.r = row

    def __add__(self, other):
        print('Сумма клеток равна:')
        return Cell(self.p + other.p, self.r)

    def __sub__(self, other):
        print('Разность клеток равна:')
        return Cell(self.p - other.p if self.p - other.p > 0 else 'разность меньше ноля', self.r)

    def __mul__(self, other):
        print('Произведение клеток равно:')
        return Cell(self.p * other.p, self.r)

    def __truediv__(self, other):
        print('Деление клеток равно:')
        return Cell(round(self.p / other.p, 0), self.r)

    def __str__(self):
        return f"{self.p}"

    @property
    def make_order(self):
        print(f'Клетка {self.p} ячеек и {self.r} ряда')
        res = ("*" * self.r + "\n") * (self.p // self.r) + ("*" * (self.p % self.r) + "\n")
        return f'{res}'


c_1 = Cell(7, 3)
c_2 = Cell(6, 3)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1.make_order)
print(c_2.make_order)
