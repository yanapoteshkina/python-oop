class Vector:
    MIN_CORD = 0
    MAX_CORD = 100

# classmethod - работает с атрибутами класса и может вызываться в др
# методах класса но он не имеет право на локальные переменные методов класса
    @classmethod
    def validate(cls, arg):
        return cls.MIN_CORD <= arg <= cls.MAX_CORD

    def __init__(self, x, y):
        self.x = self.y = 0

        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
    def get_cord(self):
        return self.x, self.y

#данная функция работает вне зависимости от атрибутов класса или локальных переменных
    @staticmethod
    def norm2(x,y):
        return x*x + y*y


v = Vector(1, 200)
print(Vector.validate(5))
res = Vector.get_cord(v)
print(res)