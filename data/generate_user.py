import allure
import random
import string


@allure.title("Генерируем данные для создания пользователя")
def generate_data_for_new_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    name = generate_random_string(7)
    email = name + '@yandex.ru'
    password = generate_random_string(7)

    payload = {
        "name": name,
        "email": email,
        "password": password
    }
    return payload
