from address import Address
from airplane import Airplane
from flight import Flight
from passager import Passenger
from faker import Faker
import random

fake = Faker('pt_BR')

def create_flight_instances(num_flights=10):
    """
    Cria voos
    num_flights: número de voos a serem criados
    """
    flights = []
    
    # Cidades separadas por (Cidade, SIGLA, CEP)
    cities = [
        ("São Paulo", "SP", "01310-200"),
        ("Rio de Janeiro", "RJ", "22021-001"),
        ("Brasília", "DF", "70040-010"),
        ("Salvador", "BA", "40070-110"),
        ("Fortaleza", "CE", "60165-081"),
        ("Belo Horizonte", "MG", "30130-100"),
        ("Curitiba", "PR", "80010-000"),
        ("Manaus", "AM", "69005-000"),
        ("Recife", "PE", "50010-000"),
        ("Porto Alegre", "RS", "90010-000"),
    ]
    
    for i in range(num_flights):
        # Criar endereços simples
        origin_city = random.choice(cities)
        destination_city = random.choice([c for c in cities if c != origin_city]) # Destino é diferente da origem
        
        origin = Address("Aeroporto", 1, origin_city[1], origin_city[0], origin_city[2])
        destination = Address("Aeroporto", 1, destination_city[1], destination_city[0], destination_city[2])
        
        # Criar aeronave com tripulação aleatória
        # has_crew = random.choice([True, False])
        has_crew = True # Forçando sempre com tripulação para ter 100% de alocação.
        airplane = Airplane(i + 1, f"Avião-{i+1}", 50, crewing=has_crew)
        
        
        # Codigo de voo Aleatório
        # A: 1 letra + 4 números + 2 letras
        # Exemplo: A1234BC
        code = f"{fake.random_uppercase_letter()}{fake.random_int(min=1000, max=9999)}{fake.random_uppercase_letter()*2}"
        
        # Adicionando o i da iteração, garantindo que seja unico
        flight_code = f"{code}-{i}"
        
        flight = Flight(flight_code, origin, destination, airplane)
        flights.append(flight)
        
        crew_status = "✅ COM TRIPULAÇÃO" if has_crew else "❌ SEM TRIPULAÇÃO"
        print(f"Voo {flight_code}: {origin_city[0]} ({origin_city[1]}) → {destination_city[0]} ({destination_city[1]}) | {crew_status}")
    
    return flights


def create_passengers(num_passengers=250):
    """
    Cria passageiros simples utilizando a lib Faker
    num_passengers: número de passageiros a serem criados   
    """
    passengers = []
    
    for i in range(num_passengers):
        name = fake.name()
        cpf = fake.ssn()
        address = Address("Rua A", 123, "SP", "São Paulo", "01010-101")
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%d-%m-%Y")
        
        passenger = Passenger(i + 1, name, cpf, address, birth_date)
        passengers.append(passenger)
    
    return passengers


def allocate_passengers_to_available_flights(flights, passengers):
    """
    Aloca passageiros
    flights: lista de voos
    passengers: lista de passageiros
    """
    allocated = 0
    
    for passenger in passengers:
        # Filtrando voos disponíveis e COM TRIPULAÇÃO
        available_flights = [f for f in flights 
                           if f.get_passengers_count() < f.airplane.capacity 
                           and f.airplane.is_crewing()]
        
        if available_flights:
            selected_flight = random.choice(available_flights)
            selected_flight.add_passenger(passenger)
            
            # Alocar assento
            available_seats = selected_flight.get_available_seats()
            if available_seats:
                seat_id = random.choice(available_seats)
                passenger.seat_number = seat_id
                selected_flight.airplane.seats[seat_id].occupy_seat()
                allocated += 1
                print(f"✅ {passenger.name} → Voo {selected_flight.flight_number}, Assento {seat_id}")
            else:
                print(f"❌ {passenger.name} → Sem assentos no voo {selected_flight.flight_number}")
        else:
            print(f"❌ {passenger.name} → Nenhum voo COM TRIPULAÇÃO disponível")
    
    return allocated


def display_allocation_summary(flights, total_allocated, total_passengers):
    """
    Imprime o resumo
    flights: lista de voos
    total_allocated: total de passageiros alocados
    total_passengers: total de passageiros
    """
    print("\n" + "="*60)
    print("📊 RESUMO")
    print("="*60)
    
    print(f"👥 Passageiros alocados: {total_allocated}/{total_passengers}")
    print(f"🛫 Total de voos: {len(flights)}")
    
    flights_with_crew = [f for f in flights if f.airplane.is_crewing()]
    flights_without_crew = [f for f in flights if not f.airplane.is_crewing()]
    
    print(f"✅ Voos com tripulação: {len(flights_with_crew)}")
    print(f"❌ Voos sem tripulação: {len(flights_without_crew)}")
    
    print("\n📋 STATUS POR VOO:")
    for flight in flights:
        crew_status = "✅" if flight.airplane.is_crewing() else "❌"
        passengers_count = flight.get_passengers_count()
        capacity = flight.airplane.capacity
        
        print(f"  {crew_status} Voo {flight.flight_number}: {passengers_count}/{capacity} passageiros")
        
        # Mostrar voos sem tripulação que não podem operar
        if not flight.airplane.is_crewing() and passengers_count > 0: # nao aparecece pois estamos forcando sempre com tripulação
            print(f"⚠️  ATENÇÃO: Voo sem tripulação mas com passageiros!")
    
    print(f"\n🎯 Taxa de alocação: {(total_allocated/total_passengers)*100:.1f}%")
    print("="*60)


def main():
    """Função principal do sistema de alocação de passageiros"""
    print("🚀 SISTEMA DE ALOCAÇÃO DE PASSAGEIROS")
    print("=" * 50)
    passengers_int = 250
    flights_int = 10

    print(f"\n📋 Criando {flights_int} voos...")
    flights = create_flight_instances(flights_int)

    print(f"\n👥 Criando {passengers_int} passageiros...")
    passengers = create_passengers(passengers_int)

    print(f"\n🎯 Alocando passageiros (apenas em voos COM TRIPULAÇÃO)...")
    total_allocated = allocate_passengers_to_available_flights(flights, passengers)
    
    display_allocation_summary(flights, total_allocated, len(passengers))


if __name__ == "__main__":
    main()