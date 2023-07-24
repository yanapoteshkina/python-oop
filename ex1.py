class House:
     "Класс вид Домов"

#Атрибуты/свойства класса
     theme = 'Color mode'
     author = 'Name '
     city = 'City'

#Создание экземпляра класса
house1 = House()
house2 = House()

#Через свойство экземпляр класса, назначаем новое свойство класа, создавая в просранстве экземпляра значение
house1.theme = 'pink mode'
house1.theme = 'dark mode'

# Если атрибута не сущсетвует, то он создается, можно также для этого использовать setattr
# setattr(House, styleHome, 'Korean')
House.styleHome = 'Korean'

#getattr(obj, name, [default]) - возвращает значение атрибута обьекта
#hasattr(obj, name) - проверяет на наличие атрибута name в obj
#setattr(obj, name, value) - задает значение атрибута (если атрибута не сущсетвует, то он создается)
#delattr(obj, name) - удаляет атрибут с именем name

#.__doc__ - содержит строку с описанием класса
#.__dict__ - содержит набор атрибутов экземпляра класса
