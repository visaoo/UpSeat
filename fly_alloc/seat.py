class Seat:
    def __init__(self, seat_id, seat_class="Economica"):
        self.seat_id = seat_id  # Ex: "F5E"
        self.seat_class = seat_class
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True

    def vacate(self):
        self.is_occupied = False

    def __str__(self):
        status = "Ocupado" if self.is_occupied else "Livre"
        return f"Assento: {self.seat_id} ({self.seat_class}) - Status: {status}"
    

seat = Seat("F532E", "Executiva")  # Cria um assento com ID "F532E" na classe Executiva
print(seat)  # Exibe o estado inicial do assento
seat.occupy()  # Marca o assento como ocupado
print(seat)  # Exibe o estado do assento após ocupação
seat.vacate()  # Marca o assento como livre novamente
print(seat)  # Exibe o estado do assento após desocupação