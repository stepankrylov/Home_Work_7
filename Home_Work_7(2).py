class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def fabric(self):
        size_coat = round(self.v / 6.5 * 0.5, 2)
        size_costume = round(2 * self.h + 0.3, 2)
        return f'Для пальто: {size_coat} кв.м.\n' \
               f'Для костюма: {size_costume} кв.м.\n' \
               f'Итого: {size_coat + size_costume} кв.м.'


c = Clothes(48, 1.72)
print(c.fabric)
