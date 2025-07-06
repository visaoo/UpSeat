class Seat:
    def __init__(self, seat_id, seat_class="Economica", is_occupied=False):
        self.seat_id = seat_id  # Ex: "F5E"
        self.seat_class = seat_class
        self.is_occupied = is_occupied

    def occupy(self):
        self.is_occupied = True

    def vacate(self):
        self.is_occupied = False

    def __str__(self):
        status = "Ocupado" if self.is_occupied else "Livre"
        return f"Assento: {self.seat_id} ({self.seat_class}) - Status: {status}"