from constants import API_POST_MANY_EXPENSES_ENDPOINT, API_GET_ALL_EXPENSES
import requests

def insert_many_expenses(data):
    response = requests.post(API_POST_MANY_EXPENSES_ENDPOINT, json=data)

    response.raise_for_status()

    return {
        'success': True,
        'data': response.json() if response.content else None,
        'status_code': response.status_code
    }

def get_all_expenses():
    response = requests.get(API_GET_ALL_EXPENSES)

    response.raise_for_status()

    return {
        'success': True,
        'data': response.json() if response.content else None,
        'status_code': response.status_code
    }
