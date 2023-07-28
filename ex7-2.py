#КЛАСС КАК ПРОСТРАНСТВО ИМЕН
#магические методы для атрибутов класса

#- __setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса

#- __getattribute__(self, item) - автоматически вызывается при получении свойства класса именем item

# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса

# __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно: существует оно ли нет)



class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    #этот метод атрибута автоматически вызывается когда идет считывание атрибута через экземпляр класса
    def __getattribute__(self, item):
        #с помощью этого метода мы можем управлять значение к тому или иному атрибуту
        if item == "x":
            raise ValueError("доступ запрещен")
        else:
            # без return возращает none
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

            #Если вместо object.__setattr__(self, key, value)
            # Записать только - self.x = value
            #то метод будет вызываться по рекурсии каждый раз

#если мы не хотим чтобы при создании несущетвующего атрибута появляла ошибка и это как-то обрабатывалось, рекомен использовать эту функцию
    def __getattr__(self, item):
        print("__getattr__:" + item)

#вызывается при удалении атрибута класса
    def __delattr__(self, item):
        print("__delattr__" +item)
        #чтобы произошла удаление надо произвести операцию
        object.__delattr__(self, item)


pt1 = Point(1, 2)

#setattr
#pt1.z = 5

#getattr - вызов не существующего атрибута
print(pt1.yy)

#delattr
del pt1.x
print(pt1.__dict__)