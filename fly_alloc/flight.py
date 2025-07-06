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
    def __init__(self, flight_number: str, origin: Address, destination: Address, airplane: Airplane, paid: bool = False):
        self._flight_number = flight_number
        self._origin = origin
        self._destination = destination
        self._airplane = airplane
        self._passengers = []  # Lista de passageiros
        self._paid = paid
        self._status = FlightStatus.SCHEDULED
        
    def _update_status(self, status: FlightStatus) -> None:
        """Atualiza o status do voo"""
        if not isinstance(status, FlightStatus):
            raise TypeError("O status deve ser uma instância da classe FlightStatus.")
        self._status = status

    def add_passenger(self, passenger) -> None:
        """Adiciona um passageiro ao voo"""
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
        if passenger not in self._passengers:
            raise ValueError("O passageiro não está no voo.")
        if not self._airplane.is_seat_available(seat_id):
            raise ValueError("Assento não disponível.")
        self._airplane.allocate_seat(seat_id)
        passenger.seat_number = seat_id  # Atribui o assento ao passageiro
        return True 
    
    def get_available_seats(self) -> list:
        """Retorna uma lista de assentos disponíveis no voo"""
        return [seat_id for seat_id, seat in self._airplane.seats.items() if not seat.is_occupied]

    def seat_count(self) -> int:
        """Retorna o número de assentos disponíveis no voo"""
        return self._airplane.get_seat_count()
    
    def get_flight_info(self) -> str:
        """Retorna informações do voo"""
        return f"Informações do voo: {self._flight_number}, Origem: {self._origin}, Destino: {self._destination}, Aeronave: {self._airplane.model}, Capacidade: {self._airplane.capacity}"

    def __str__(self) -> str:
        return f"Voo {self._flight_number} de {self._origin} para {self._destination}, Aeronave: {self._airplane.model}"


if __name__ == "__main__":
    flight_number="FL123"
    origin = Address("Avenida Brasil", "123", "São Paulo", "SP", "01000-000")
    destination = Address("Rua das Flores", "456", "Rio de Janeiro", "RJ", "20000-000")
    airplane = Airplane(id=1, model="Boeing 737", capacity=250)
    
    passager1 = Passenger(id=1, name="João Silva", cpf="123.456.789-00", address=Address("Rua A", "10", "São Paulo", "SP", "01000-000"))
    passager2 = Passenger(id=2, name="Maria Oliveira", cpf="987.654.321-00", address=Address("Rua B", "20", "Rio de Janeiro", "RJ", "20000-000"))   

    flight = Flight(flight_number, origin, destination, airplane)
    print(flight.get_flight_info())
    flight.add_passenger(passager1)
    flight.add_passenger(passager2)
    print(flight)
    print(f"Assentos disponíveis: {len(flight.get_available_seats())}")
    flight.allocate_seat(passager1, "1A")
    flight.allocate_seat(passager2, "3B")
    print(f"Assentos disponíveis após alocação: {len(flight.get_available_seats())}")
    print(passager1.seat_number)
    print(passager2.seat_number)