# Родительский класс "Человек"
class Human:
    def __init__(self, surname, name, age=None):
        """
        Инициализация объекта класса Human.
        :param surname: Фамилия (str)
        :param name: Имя (str)
        :param age: Возраст (int), опционально
        """
        if not isinstance(name, str) or not name.isalpha() or not name[0].isupper():
            raise ValueError("Некорректное значение имени")
        self.name = name

        if not isinstance(surname, str) or not surname.isalpha() or not surname[0].isupper():
            raise ValueError("Некорректное значение фамилии")
        self.surname = surname

        if age is not None:
            if not isinstance(age, int) or not (0 <= age <= 150):
                raise ValueError("Возраст должен быть целым числом от 0 до 150")
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname}, Возраст: {self.age if self.age is not None else 'Не указан'}"

    def __repr__(self):
        return f"Human('{self.surname}', '{self.name}', {self.age})"


# Класс "Студент", наследник класса Human
class Student(Human):
    def __init__(self, surname, name, age=None, number_of_debts=0):
        """
        Инициализация объекта класса Student.
        :param number_of_debts: Количество долгов (int)
        """
        super().__init__(surname, name, age)

        if not isinstance(number_of_debts, int) or not (0 <= number_of_debts <= 15):
            raise ValueError("Количество долгов должно быть числом от 0 до 15")
        self.number_of_debts = number_of_debts

    def __str__(self):
        human_info = super().__str__()
        return f"{human_info}, Долги: {self.number_of_debts}"

    def __repr__(self):
        return f"Student('{self.surname}', '{self.name}', {self.age}, {self.number_of_debts})"

