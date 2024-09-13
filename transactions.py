import requests
from datetime import datetime
from config import TOKEN, ACCOUNT_ID 

class Transaction:
    def __init__(self, id, time, description, mcc, originalMcc, amount, operationAmount, currencyCode, commissionRate, cashbackAmount, balance, hold, counterName):
        self.id = id
        self.time = datetime.fromtimestamp(time).strftime('%H:%M:%S')
        self.description = description
        self.mcc = mcc
        self.originalMcc = originalMcc
        self.amount = int(amount / 100)
        self.operationAmount = int(operationAmount / 100)
        self.currencyCode = currencyCode
        self.commissionRate = commissionRate
        self.cashbackAmount = cashbackAmount
        self.balance = balance
        self.hold = hold
        self.counterName = counterName

    def __repr__(self):
        return f"Transaction(time={self.time}, description={self.description}, amount={self.amount})"


def transform_to_objects(transactions):
    return [Transaction(**transaction) for transaction in transactions]



def get_transactions():
    API_TOKEN = TOKEN
    account_id = ACCOUNT_ID

    MONOBANK_API_URL = "https://api.monobank.ua/personal/statement/{account_id}/{from_date}/{to_date}"

    headers = {
        'X-Token': API_TOKEN
    }

    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    from_date = int(start_of_day.timestamp())
    to_date = int(now.timestamp())

    try:
        response = requests.get(MONOBANK_API_URL.format(account_id=account_id, from_date=from_date, to_date=to_date), headers=headers)

        if response.status_code == 200:
            transactions = response.json()
            
            return transform_to_objects(transactions)
        else:
            print(f"Ошибка: {response.status_code}, сообщение: {response.text}")
            return []
    except Exception as e:
        print(f"Произошла ошибка при запросе: {str(e)}")
        return []


