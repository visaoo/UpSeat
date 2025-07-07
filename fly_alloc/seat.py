from enum import Enum


class seatClass(Enum):
    """Classe para gerenciar o tipo de assento"""
    ECONOMICA = "Economica"
    EXECUTIVA = "Executiva"
    PRIMEIRA_CLASSE = "Primeira Classe"

class Seat:
    def __init__(self, seat_id: str, seat_class: seatClass = seatClass.ECONOMICA, is_occupied: bool = False):
        self._seat_id = seat_id
        self._seat_class = seat_class
        self._is_occupied = is_occupied

    @property
    def seat_id(self) -> str:
        """Retorna o ID do assento."""
        return self._seat_id

    @property
    def seat_class(self) -> seatClass:
        """Retorna a classe do assento (Ex: Economica, Executiva)."""
        return self._seat_class

    @property
    def is_occupied(self) -> bool:
        """Retorna True se o assento estiver ocupado, False caso contrário."""
        return self._is_occupied

    def occupy_seat(self) -> bool:
        """
        Tenta ocupar o assento.
        Retorna True se o assento foi ocupado com sucesso, False se já estava ocupado.
        """
        if not self._is_occupied:
            self._is_occupied = True
            print(f"Assento {self._seat_id} agora está ocupado.")
            return True
        else:
            print(f"Assento {self._seat_id} já está ocupado.")
            return False

    def vacate_seat(self) -> bool:
        """
        Tenta liberar o assento.
        Retorna True se o assento foi liberado com sucesso, False se já estava livre.
        """
        if self._is_occupied:
            self._is_occupied = False
            print(f"Assento {self._seat_id} agora está livre.")
            return True
        else:
            print(f"Assento {self._seat_id} já está livre.")
            return False

    def __str__(self) -> str:
        """Retorna uma representação em string do assento."""
        status = "Ocupado" if self._is_occupied else "Livre"
        return f"Assento: {self._seat_id} ({self._seat_class}) - Status: {status}"

    def __repr__(self) -> str:
        """Retorna uma representação oficial do objeto para depuração."""
        return f"Seat(seat_id='{self._seat_id}', seat_class='{self._seat_class}', is_occupied={self._is_occupied})"