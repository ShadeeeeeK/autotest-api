from faker import Faker

fake = Faker('ru_RU')

data = {
    "email": fake.email(),
    "name": fake.name(),
    "age": fake.random_int(18, 65)
}

