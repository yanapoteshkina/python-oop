#В программе должен существовать только один экземпляр класса

class DataBase:
    #атрибут класса который станет ссылкой на экземпляр класса как флажок
    __instance = None

    def __new__(cls, *args, **kwargs):
        print("new - method")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None
        print("Удаление" + str(self))

    def __init__(self, user, psw, port):
    #инициализация экземпляра класса, атрибуты:
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД:{self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Закрытие соединения с БД")

    def read(self):
        print("Данные из БД")

    def write(self, data):
        print(f"запись в БД {data}")

db=DataBase('us', '1234', 80)
db2=DataBase('us2', '1234', 40)

db.connect()
db2.connect()
