from accessify import private, protected

class RegisterNum():

    def __init__(self, phone):
        self.__phone = 0
        if self.check_value(phone):
            self.__phone = phone

    @private
    @classmethod
    def check_value(cls, phone):
        return type(phone) in (int, float)

    def set_phone(self, phone):
        if self.check_value(phone):
            self.__phone = phone
        else:
            raise ValueError("Значение должно быть цифрой")

    def get_phone(self):
        return print(self.__phone)


num = RegisterNum(87770543266)

num.set_phone(87770543235)
num.get_phone()

print(dir(num))
num.check_value(5)


