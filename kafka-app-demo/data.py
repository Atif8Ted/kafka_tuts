from faker import Faker

fake = Faker()


def get_registered_user():
    user_data = {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year(),
    }
    return user_data
