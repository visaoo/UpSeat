from faker import Faker
from fly_alloc.airplane import Airplane

fake = Faker()

def test_airplane_creation():
    airplane = Airplane(
        id=fake.random_int(min=1, max=9999999),
        model=fake.word(),
        capacity=fake.random_int(min=50, max=300)
    )
    
    return airplane 


x = test_airplane_creation()

print(len(x._view_seats()))
print(x._capacity)
print(x._model)
print(x._id)