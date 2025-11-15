from faker import Faker
users = []
def generate_users(n):
    faker = Faker()
    for _ in range(n):
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        }
        users.append(user)

generate_users(5)
for i, user in enumerate(users, start=1):
    print(f"Utilisateur {i}:")
    print(f"  Nom: {user['name']}")
    print(f"  Adresse: {user['address']}")
    print(f"  Langue: {user['language_code']}")
    print("-" * 40)