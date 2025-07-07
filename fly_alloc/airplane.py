from seat import Seat
from seat import seatClass

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from seat import seatClass

### IDEIA 

# Quero que dentro da aeronave de para ver assentos ocupados e livres
# depois de verificar se o assento esta livre, vincular o assento a um passageiro

class Airplane:
    def __init__(self, id: int, model: str, capacity: int, crewing: bool = False):
        self._id = id
        self._model = model
        self._capacity = capacity
        self._seats = self._generate_seats()
        self._crewing = crewing


    def _generate_seats(self):
        """
        Gera os assentos da aeronave com base na capacidade definida.
        Cada assento é identificado por um ID no formato "1A", "1B",
        "1C", etc., e é atribuído à classe econômica por padrão.
        """
        seats = {}
        columns = ['A', 'B', 'C', 'D', 'E', 'F']
        
        for i in range(self._capacity):
            row = (i // len(columns)) + 1  # Calcula a fileira
            col = columns[i % len(columns)]  # Calcula a coluna
            seat_id = f"{row}{col}"
            seats[seat_id] = Seat(seat_id, seatClass.ECONOMICA, False)

        return seats
    
    @property
    def id(self):
        return self._id
    
    @property
    def model(self):
        return self._model
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def seats(self):
        return self._seats
    
    def get_seat_count(self):
        """Returns the total number of seats available"""
        return len(self._seats)
    
    def is_seat_available(self, seat_id: str) -> bool:
        """Checks if a specific seat is available"""
        if seat_id not in self._seats:
            raise ValueError(f"Seat {seat_id} does not exist.")
        return not self._seats[seat_id].is_occupied

    def allocate_seat(self,  seat_id: str) -> bool:
        """Aloca um assento para um passageiro"""
        if seat_id not in self._seats:
            raise ValueError(f"Seat {seat_id} does not exist.")
        if self._seats[seat_id].is_occupied:
            raise ValueError(f"Seat {seat_id} is already occupied.")
        self._seats[seat_id].occupy_seat()
        return True

    def __str__(self):
        return f"Aeronave {self._model} (ID: {self._id}) - Capacidade: {self.get_seat_count()} assentos"