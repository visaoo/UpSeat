from abc import ABC, abstractmethod


class AddressInterface(ABC):
    """Interface para endereços"""
    
    @abstractmethod
    def get_full_address(self) -> str:
        """Retorna endereço completo formatado"""
        pass
    
    @abstractmethod
    def validate_address(self) -> bool:
        """Valida o endereço"""
        pass

class Address(AddressInterface):
    def __init__(self, street, number, city, state, zip_code):
        self._street = street
        self._number = number
        self._city = city
        self._state = state
        self._zip_code = zip_code

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value
        
    def get_full_address(self):
        """Implementação padrão do endereço completo"""
        return f"{self._street}, {self._number} - {self._city}/{self._state} - {self._zip_code}"
    
    def validate_address(self) -> bool:
        """Validação básica do endereço"""
        required_fields = [self._street, self._number, self._city, self._state, self._zip_code]
        return all(field.strip() for field in required_fields)
            
        
    def to_dict(self):
        return {
            "street": self._street,
            "number": self._number,
            "city": self._city,
            "state": self._state,
            "zip_code": self._zip_code
        }

    def __str__(self):
        return f"{self._street}, {self._number}, {self._city}, {self._state}, {self._zip_code}"