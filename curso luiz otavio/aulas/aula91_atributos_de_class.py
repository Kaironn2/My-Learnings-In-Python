class User():
    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return User.current_year - self.age


user1 = User('Braia Binga M', 22)
user2 = User('Braia Binga S', 27)

print(user1.get_birth_year())
print(user2.get_birth_year())
