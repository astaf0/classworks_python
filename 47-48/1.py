# class Person():
#     def __init__(self, name):
#         self.name = name
#
# p = Person('Алиса')
# print(p.name)

class Secret:
    def __init__(self):
        self.__code = '1234'

s = Secret()
s.__code()