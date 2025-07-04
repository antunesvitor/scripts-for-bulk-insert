from api_calls import expenses as expense_api
from constants import API_URL
from data_sanitization import data_sanitize as san
import glob

def main(filenames):
    for filename in filenames:
        filename_lower = filename.lower()

        if "debito" in filename_lower:
            body_data = san.sanitize_debito(filename)
            api_response = expense_api.insert_many_expenses(body_data)
            print(f'success return for {filename}: {api_response['success']}')
        elif "credito" in filename_lower:
            body_data = san.sanitize_credito(filename)
            api_response = expense_api.insert_many_expenses(body_data)
            print(f'success return for {filename}: {api_response['success']}')
        else:
            print (f"{filename} is not recognized file")

if __name__ == '__main__':
    csv_files = glob.glob('data/*.csv')
    main(csv_files)

    # print(expenses.get_all_expenses())
