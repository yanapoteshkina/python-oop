class House:
    theme = 'ee'
    author = 'de'

#инициализатор обьекта класаа/ вызывается после создания обьекта
    def __init__(self, x = 0, y =0):
        print("init" + str(self))
        self.x = x
        self.y = y
#финализатор обьекта класса
    def __del__(self):
        print("удаление экземпляра:" + str(self))

pt = House(1,6)



print(pt.__dict__)