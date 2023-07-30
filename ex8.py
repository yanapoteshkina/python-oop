#Паттрен Моносостояние

class ThreadData:
    __shared_attr = {
        'name': '',
        'data': {},
        'id': 1
    }
    def __init__(self):
        #создание общего просранства имен которое будет связано даже при изменение свойств отдельных экземпляров
        self.__dict__ = self.__shared_attr

td = ThreadData()
td1= ThreadData()
td.id = 44
