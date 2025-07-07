from person import Person


class Passenger(Person):
    """Classe que representa um passageiro, herdando de Person"""
    
    def __init__(self, id: int, name: str, cpf: str, address, birth_date: str = '', seat_number: str = ''):
        super().__init__(name, cpf, address, birth_date)
        self._id = id
        self._seat_number = seat_number

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def seat_number(self) -> str:
        return self._seat_number
    
    @seat_number.setter
    def seat_number(self, seat_number: str) -> None:
        """Atribui um assento ao passageiro"""
        self._seat_number = seat_number
    
    def remove_seat(self) -> None:
        """Remove a atribuição de assento"""
        self._seat_number = ''
    
    @property
    def has_seat(self) -> bool:
        """Verifica se o passageiro tem assento atribuído"""
        return bool(self._seat_number)
    
    # def get_role(self) -> str:
    #     """Retorna o papel/tipo da pessoa"""
    #     return "Passageiro"
    
    def to_dict(self):
        """Converte para dicionário incluindo informações de passageiro"""
        data = super().to_dict()
        data.update({
            "id": self._id,
            "seat_number": self._seat_number,
            "has_seat": self.has_seat
        })
        return data

    def __str__(self):
        person_info = super().__str__()
        seat_info = f", Assento: {self._seat_number}" if self._seat_number else ", Sem assento"
        return f"Passageiro {self._id} - {person_info}{seat_info}"
