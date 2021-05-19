class Student:

    def __init__(self, name, user, email):
        self._name = name
        self._user = user
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def user(self):
        return self._user

    @property
    def email(self):
        return self._email

    def __str__(self):
        return f'Nome: {self._name} | username: {self._user} | e-mail: {self._email}'
