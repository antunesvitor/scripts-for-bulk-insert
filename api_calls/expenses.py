"""Module providing interface to call expenses API."""

import requests
from constants import API_POST_MANY_EXPENSES_ENDPOINT, API_GET_ALL_EXPENSES

def insert_many_expenses(data):
    """
    Calls endpoint to bulk insert expenses
    """
    try :
        response = requests.post(API_POST_MANY_EXPENSES_ENDPOINT, json=data, timeout=10)

        response.raise_for_status()

        return {
            'success': True,
            'data': response.json() if response.content else None,
            'status_code': response.status_code
        }
    except requests.exceptions.HTTPError as http_err:
        print(f'error occured: {http_err}')
        print(f'response body: {response.text}')
        return {
            'success': False,
            'data': response.json() if response.content else None,
            'status_code': response.status_code
        }
    except Exception as err:
        print(f"An other error occurred: {err}")
        return {
            'success': False,
            'data': err,
            'status_code': response.status_code
        }

def get_all_expenses():
    response = requests.get(API_GET_ALL_EXPENSES,timeout=10)

    response.raise_for_status()

    return {
        'success': True,
        'data': response.json() if response.content else None,
        'status_code': response.status_code
    }
