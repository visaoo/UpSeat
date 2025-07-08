from abc import ABC, abstractmethod
from enum import Enum
from address import Address
from airplane import Airplane
from passager import Passenger

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from address import Address
    from airplane import Airplane
    from passager import Passenger

class FlightStatus(Enum):
    """Classe para gerenciar o status do voo"""
    SCHEDULED = "Scheduled"
    DELAYED = "Delayed"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

class FlightInterface(ABC):
    """Interface para a classe Flight"""

    @abstractmethod 
    def get_flight_info(self) -> str:
        """Retorna informações do voo"""
        pass
    @abstractmethod
    def __str__(self) -> str:
        """Representação em string do voo"""
        pass

class Flight(FlightInterface):
    def __init__(self, flight_number: str, origin: Address, destination: Address, airplane: Airplane):
        self._flight_number = flight_number
        self._origin = origin
        self._destination = destination
        self._airplane = airplane
        self._passengers = []  # Lista de passageiros
        self._status = FlightStatus.SCHEDULED
        
    def _update_status(self, status: FlightStatus) -> None:
        """Atualiza o status do voo"""
        if not isinstance(status, FlightStatus):
            raise TypeError("O status deve ser uma instância da classe FlightStatus.")
        self._status = status

    def add_passenger(self, passenger) -> None:
        """Adiciona um passageiro ao voo"""
        if self._airplane.capacity <= len(self._passengers):
            return # Não adiciona se a capacidade do voo já foi atingida
        if not isinstance(passenger, Passenger):
            raise TypeError("O passageiro deve ser uma instância da classe Passenger.")
        self._passengers.append(passenger)
        
    def remove_passenger(self, passenger: Passenger) -> bool:
        """Remove um passageiro do voo"""
        if passenger in self._passengers:
            self._passengers.remove(passenger)
            return True
        else:
            raise ValueError("O passageiro não está no voo.")

    def allocate_seat(self, passenger: Passenger, seat_id: str) -> bool:
        """Aloca um assento para um passageiro"""
        print(passenger.name)
        if passenger not in self._passengers:
            raise ValueError("O passageiro não está no voo.")
        if not self._airplane.is_seat_available(seat_id):
            raise ValueError("Assento não disponível.")
        passenger.seat_number = seat_id  # Atribui o assento ao passageiro
        return True 
    
    def get_available_seats(self) -> tuple:
        """Retorna uma lista de assentos disponíveis no voo"""
        return tuple(seat_id for seat_id, seat in self._airplane.seats.items() if not seat._is_occupied)
    
    def get_occupied_seats(self) -> tuple:
        """Retorna uma lista de assentos ocupados no voo"""
        return tuple(seat_id for seat_id, seat in self._airplane.seats.items() if seat._is_occupied)

    def seat_count(self) -> int: 
        # Provavelmente não é necessário, mas pode ser útil
        """Retorna o número de assentos disponíveis no voo"""
        return self._airplane.get_seat_count()
    
    @property
    def flight_number(self) -> str:
        """Retorna o número do voo"""
        return self._flight_number
    
    @property
    def passengers(self) -> list:
        """Retorna a lista de passageiros do voo"""
        return self._passengers.copy()  # Retorna uma cópia para não permitir modificação direta
    
    @property
    def airplane(self):
        """Retorna a aeronave do voo"""
        return self._airplane # WARN!! Retorna a instancia.
    
    @property
    def origin(self):
        """Retorna o endereço de origem"""
        return self._origin
    
    @property
    def destination(self):
        """Retorna o endereço de destino"""
        return self._destination
    
    def get_passengers_count(self) -> int:
        """Retorna o número de passageiros no voo"""
        return len(self._passengers)

    def get_flight_info(self) -> str:
        """Retorna informações do voo"""
        return f"Informações do voo: {self._flight_number}, Origem: {self._origin}, Destino: {self._destination}, Aeronave: {self._airplane.model}, Capacidade: {self._airplane.capacity}"

    def __str__(self) -> str:
        return f"Voo {self._flight_number} de {self._origin} para {self._destination}, Aeronave: {self._airplane.model}"