import requests
from config import TOKEN

# Твой ключ API
API_TOKEN = TOKEN

# URL Monobank API для получения информации о пользователе и счетах
MONOBANK_API_URL = "https://api.monobank.ua/personal/client-info"

# Заголовки для авторизации
headers = {
    'X-Token': API_TOKEN
}

# Выполняем запрос
response = requests.get(MONOBANK_API_URL, headers=headers)

if response.status_code == 200:
    client_info = response.json()
    accounts = client_info['accounts']
    for account in accounts:
        print(account)

    

else:
    print(f"Ошибка: {response.status_code}, сообщение: {response.text}")
