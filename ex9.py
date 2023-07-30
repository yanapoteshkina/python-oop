#свойства property

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

#Соединение геттера и сеттера в один метод с помощью property
    #первый параметр это геттер второй сеттер
    old = property(get_old, set_old)

    # old = old.setter(set_old)
    # old = old.getter(get_old)

p = Person('Чебурек', 20)
p.old = 35
print(p.old, p.__dict__)