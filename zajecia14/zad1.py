# def sound_decorator(func_as_param):
#   def hau_nested():
#       print('Hau ~ hau')
#       func_as_param()
#   return hau_nested
#
# def pet_func():
#     print('Pies to najlepszy przyjaciel człowieka')
#
#
# pet_func()
# print('--------------')
# dog = sound_decorator(pet_func)
# dog()
#
#
# @hau_decorator
# def pet_func():
#     print('Pies to najlepszy przyjaciel człowieka')
#
#
# pet_func()


# class Student:
#     min_avg = 4.5
#     university = 'New York Academy'
#
#     def __init__(self, name, last, age, student_avg):
#         self.name = name
#         self.last = last
#         self.age = age
#         self.student_avg = student_avg
#
#     def __repr__(self):
#         return self.name.capitalize() + " " + self.last.capitalize()
#
#     def email(self):
#         return '{}.{}.university.com'.format(self.name, self.last)
#
#     def grant_scholarship(self):
#         if self.student_avg > self.min_avg:
#             print('Przyznano stypendium')
#         else:
#             print('Odmowa przyznania stypendium')
#
#
#     def set_min_avg(self, average):
#         self.min_avg = average
#
#
# obj_anna = Student('anna', 'kowalska', 23, 4.7)
# obj_arek = Student('arkadiusz', 'nowak', 21, 3.9)
# print(Student.min_avg)
# print(obj_anna.min_avg)
# print(obj_arek.min_avg)
#
# obj_anna.set_min_avg(4.8)
# print('Min srednia dla obiektu anna', obj_anna.min_avg)
# print('Min srednia dla obiektu arek', obj_arek.min_avg)

import datetime
import holidays

# today = datetime.date.today()
# print(today)
#
# pl_holidays = holidays.Polish()
# if '1/1/2019' in pl_holidays:
#     print('git')
# else:
#     print("nie git")


class Student:
    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age

    def __repr__(self):
        return f'Student: {self.name.capitalize()} {self.last.capitalize()}'

    @property
    def email(self):
        return f'{self.name}.{self.last}@university.com'

    @property
    def fullname(self):
        return f'{self.last}.{self.name}'

    @fullname.setter
    def fullname(self, last_name):
        self.last, self.name = last_name.split()

    @fullname.deleter
    def fullname(self):
        self.last, self.name = None, None
        print('deleted')


obj_anna = Student('ana', 'kowalska', 23)
print(obj_anna)
print(obj_anna.email)

obj_anna.fullname = 'zamezna Anna'
print(obj_anna)

