class Professor:

    def __init__(self, user_id, name, department):
        self._user_id = user_id
        self._name = name
        self._department = department

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def department(self):
        return self._department

    def __str__(self):
        return f'SIAPE: {self._user_id} | Nome: {self._name} | Departamento: {self._department}'
