class Subject:

    def __init__(self, subject_id, name, slots, slots_freshmen):
        self._subject_id = subject_id
        self._name = name
        self._slots = slots
        self._slots_freshmen = slots_freshmen

    @property
    def subject_id(self):
        return self._subject_id

    @property
    def name(self):
        return self._name

    @property
    def slots(self):
        return self._slots

    @property
    def slots_freshmen(self):
        return self._slots_freshmen

    def __str__(self):
        return f'{self._name} tem {self._slots} vagas.'
