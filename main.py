# Завдання 2
# Створіть клас Circle з атрибутом radius та методом
# area, який поверне площу кола з вказаним радіусом.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        return f"Ім'я студента - {self.name} та його вік {self.age}"


student1 = Student("Іван", 20)
print(student1.print_info())
