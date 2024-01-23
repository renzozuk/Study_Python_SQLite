class Customer():
    def __init__(self, id_, name, email, phone):
        self.__id = id_
        self.__name = name
        self.__email = email
        self.__phone = phone

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    def __str__(self):
        return f'[{self.__id}] Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone}'