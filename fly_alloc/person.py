from address import Address


class Person:
    def __init__(self, name: str, cpf: str, address: Address, birth_date: str = ''):
        self._name = name
        self._cpf = cpf
        self._address = address
        self._birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
        
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value


    def to_dict(self):
        return {
            "name": self._name,
            "cpf": self._cpf,
            "address": self._address.to_dict() if isinstance(self._address, Address) else None
        }

    def __str__(self):
        return f"Name: {self._name}, CPF: {self._cpf}, Address: {self._address}"
