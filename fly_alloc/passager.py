from fly_alloc.person import Person

class Passenger(Person):
    def __init__(self, id: int, name: str, cpf: str, address, birth_date: str = '', seat_number: str = ''):
        super().__init__(name, cpf, address, birth_date)
        self._id = id
        self._seat_number = seat_number

    def assign_seat(self, seat_number: str):
        self._seat_number = seat_number
        
    def to_dict(self):
        return super().to_dict() | {"id": self._id, "seat_number": self._seat_number}

    def __str__(self):
        person_info = super().__str__()
        seat_info = f", Seat: {self._seat_number}" if hasattr(self, '_seat_number') else ""
        return person_info + seat_info
