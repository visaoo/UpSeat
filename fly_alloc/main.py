from address import Address
from airplane import Airplane
from flight import Flight
from passager import Passenger
from person import Person

from faker import Faker


def main():
    ## for para gerar 30 passageiros
    airplane = Airplane(1, "Boeing 737", 250)
    airplane_origin = Address(
        "Avenida Paulista",
        1578,
        "SP",
        "São Paulo",
        "01310-200"
    )
    airplane_destination = Address(
        "Avenida Atlântica",
        1702,
        "RJ",
        "Rio de Janeiro",
        "22021-001"
    )

    flight = Flight("A2X2", airplane_origin, airplane_destination, airplane)
    
    fake = Faker()
    
    # Gerar 10 passageiros
    for i in range(10):
        name = fake.name()
        cpf = fake.ssn()
        address = Address(
            fake.street_address(),
            fake.port_number(),
            fake.city(),
            fake.state(),
            fake.zipcode(),
        )
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime(
            "%Y-%m-%d"
        )
        passengerFaker = Passenger(i+1, name, cpf, address, birth_date)
        flight.add_passenger(passengerFaker)
        
        available_seats = flight.get_available_seats()
        if available_seats:
            seat_id = available_seats[fake.random_int(0, len(available_seats) -1)]  # último disponível
            passengerFaker.seat_number = seat_id
            airplane._seats[seat_id].occupy_seat()
            print(f"Passageiro {passengerFaker.name} alocado no assento {seat_id}")
        else:
            print(f"Sem assentos disponíveis para {passengerFaker.name}")

        
    print(f"Total de passageiros alocados: {len(flight._passengers)}")
    print(f"Total de assentos ocupados: {len([seat for seat in airplane._seats.values() if seat._is_occupied])}")
    print(f"Assentos disponíveis: {len(flight.get_available_seats())}")
    print(f"Assentos: {flight.get_available_seats()}")
    print(f"Assentos ocupados: {flight.get_occupied_seats()}")

if __name__ == "__main__":
    main()