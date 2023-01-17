class Student:
    def __init__(self, name, ocenka, number):
        self.__name = name
        self.__ocenka = ocenka
        self.__number = number

    def change_grade(self, new_ocenka):
        self.__ocenka = new_ocenka

    def __repr__(self):
        return "Test name:% s number:% s ocenka:% s" % (self.__name, self.__number, self.__ocenka)
