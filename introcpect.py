# Тема "Интроспекция"
# Создание функции, которая принимает объект (любого типа) в качестве аргумента
# и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты,
# методы, модуль, и другие свойства.

from pprint import pprint


def introspection_info(obj):
    dict_info = {}
    """  Тип объекта  """
    dict_info['type'] = type(obj).__name__

    """ Атрибуты и методы объекта """
    attributes = []
    methods = []
    for value in dir(obj):
        # если value не является вызываемой функцией, значит это атрибут
        if not callable(getattr(obj, value)):
            attributes.append(value)
        # иначе это метод
        else:
            methods.append(value)
    dict_info['attributes'] = attributes
    dict_info['methodes'] = methods

    """ Модуль, к которому объект принадлежит """
    dict_info['module'] = getattr(obj, '__module__', 'None')

    return dict_info


number_info = introspection_info(42)
pprint(number_info)


# Интроспекция для объекта класса
class Persone:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)




persone = Persone("Vlad")
name = introspection_info(persone)
pprint(name)
