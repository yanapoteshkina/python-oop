class House:
    theme = ''
    author = ' '

    def set_peoples(self, x, y):
        #self - атрибут метода который получает ссылку на экземпляр класса который вызвает метод
        # Создано чтобы мы могли с локальными атрибутами конкретного экземпляра класса
        print('вызов метода set_peoples' + str(self))
        print(x + y )

#При вызове метода в экземпляре класса, интерпретатор питона передает атрибут self как
# ссылку на экземпляр кдасса который вызывает метод основного класса
# То есть при создание экземпляра класса в просрансве экземпляра класса никогда не будет создан метод,
# метод будет вызываться из основого класса а не создаваться
# По этому в основном классе всегда можно получить данные от экземпляра класса который вызывает метод у себя


house1 = House()
house1.set_peoples(10, 10)

