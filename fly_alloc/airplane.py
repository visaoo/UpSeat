class Airplane:
    def __init__(self, id, model, capacity):
        self._id = id
        self._model = model
        self._capacity = capacity
        self._seats = self._generate_seats()
    

    def _generate_seats(self):
        """
        Generates a list of seats in the format 'A1', 'A2', ..., 'B1', 'B2', ..., etc.
        """
        seats = []
        columns = ['A', 'B', 'C', 'D', 'E', 'F']
        for row in range(1, self._capacity + 1):
            for column in columns:
                seats.append(f"{column}{row}{columns[columns.index(column)-1 % len(columns)]}")
        return seats
    
    def _view_seats(self):
        """
        Returns a list of all seats in the airplane.
        """
        return self._seats


airplane = Airplane(id=1, model="Boeing 737", capacity=30)

print("Airplane Model:", airplane._model)
print("Airplane Capacity:", airplane._capacity)
print("Available Seats:", airplane._view_seats())