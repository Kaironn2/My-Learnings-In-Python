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


try:
    with open(file_path, 'r') as file_json:
        content = file_json.read()
        data = json.loads(content)
    user1 = User(**data)
    user1.name = user1.__dict__['name']
    user1.age = user1.__dict__['age']
    user1.birth = user1.get_birth_year()
    print(user1.name, user1.age, user1.birth)
except FileNotFoundError:
    print(
        f'{file_name}.json não encontrado. Por favor, crie o arquivo primeiro usando o ex27.py.')
