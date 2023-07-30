# Дескипторы

# дискриптор не данных
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

#Дескриптор данных где есть сеттеры и гетерры, дел
class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")


    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        return setattr(instance, self.name, value)

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1,2,3)
p.x = 67

print(p.xr, p.__dict__)