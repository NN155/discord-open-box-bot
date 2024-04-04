import json

login = input("login: ")
password = input("passwort: ")
# Створення словника з логіном і паролем
credentials = {
    'login': login,  # Введіть ваш логін
    'password': password  # Введіть ваш пароль
}

# Вказати шлях до файлу JSON
json_file_path = 'config.json'

# Записати дані в JSON-файл
with open(json_file_path, 'w') as json_file:
    json.dump(credentials, json_file, indent=4)


