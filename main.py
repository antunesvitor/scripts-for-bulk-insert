from api_calls import expenses
from constants import API_URL
from data_sanitization import data_sanitize as san
import glob

def main(filenames):
    for filename in filenames:
        filename_lower = filename.lower()

        if "debito" in filename_lower:
            san.sanitize_debito(filename)
        elif "credito" in filename_lower:
            # san.sanitize_credito(filename)
            print (f"work in progress for credito files")
        else:
            print (f"{filename} is not recognized file")

if __name__ == '__main__':
    csv_files = glob.glob('data/*.csv')
    main(csv_files)

    # print(expenses.get_all_expenses())
