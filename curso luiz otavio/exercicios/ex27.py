import json

file_name = 'instances'
file_path = 'C:\\Users\\rosan\\Desktop\\Py\\My-Learnings-In-Python\\Outros Arquivos\\' + file_name


class User():

    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return User.current_year - self.age


user1 = User('Jonathas', 25)
user1.__dict__['name'] = user1.name
user1.__dict__['age'] = user1.age
user1.__dict__['birth_year'] = user1.get_birth_year()

user1_dados = vars(user1)

with open(file_path, 'w') as file_json:
    json.dump(user1_dados, file_json, indent=2, ensure_ascii=False)
print('Sua lista foi exportada com sucesso!')
