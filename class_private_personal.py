import string


class Personal:
    def __init__(self, fio, age, passport, weight):
        self.fio = fio
        self.age = age
        self.passport = passport
        self.weight = weight

    @classmethod
    def check_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")
        if fio.replace(" ", "").isalpha() != True:
            raise TypeError("фИО должно состоять только из букв")
        f = fio.split(" ")
        if len(f) != 3:
            raise TypeError("ФИО должно содержать фамилию, имя и отчество через пробел")
        allsymbols = (
            string.ascii_letters
            + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        )
        if fio.replace(" ", "").strip(allsymbols) != "":
            raise TypeError("ФИО должно состоять из букв")

    @classmethod
    def check_age(cls, age):
        if type(age) != int:
            raise TypeError("Возраст должен быть целым числом")

    @classmethod
    def check_passport(cls, passport):
        if type(passport) != str:
            raise TypeError("Паспорт должен быть строкой в виде хххх хххххх")
        k = passport.split(" ")
        if len(k) != 2 or len(k[0]) != 4 or len(k[1]) != 6:
            raise TypeError(
                "Паспорт должен быть представлен в виде хххх хххххх и состоять из цифр"
            )
        if passport.replace(" ", "").isdigit() != True:
            raise TypeError("Паспорт может состоять только из чисел")

    @classmethod
    def check_weight(cls, weight):
        if type(weight) not in (int, float):
            raise TypeError("Вес должен быть целым или вещественным числом!")

    @property
    def fio(self, fio):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.check_fio(fio)
        self.__fio = fio.split(" ")

    @fio.deleter
    def fio(self, fio):
        del self.fio

    @property
    def age(self, age):
        return self.__age

    @age.setter
    def age(self, age):
        self.check_age(age)
        self.__age = age

    @age.deleter
    def age(self, age):
        del self.age

    @property
    def passport(self, passport):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.check_passport(passport)
        self.__passport = passport

    @passport.deleter
    def passport(self, passport):
        del self.passport

    @property
    def weight(self, weight):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.check_weight(weight)
        self.__weight = float(weight)

    @weight.deleter
    def weight(self, weight):
        del self.weight


Nikita = Personal("Иванов Никита Вадимович", 25, "2556 514584", 14.2)
print(Nikita.__dict__)
