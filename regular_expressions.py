"""hm14_job2"""


import re
from datetime import datetime


def find_valid_dates(file_name):
    date_pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                found_strings = re.findall(date_pattern, line)
                for date_str in found_strings:
                    try:
                        datetime.strptime(date_str, '%d.%m.%Y')
                        print(date_str)
                    except ValueError:
                        pass
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")


def is_valid_password(password):

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

    if re.match(pattern, password):
        return True
    return False


def errors_correction(text_check):
    pattern = r'\b(\w+)\s+\1\b'
    return re.sub(pattern, r'\1', text_check, flags=re.IGNORECASE)


find_valid_dates('data.txt')

while True:
    input_pass = input('Enter the password or "0" to exit: ')
    if input_pass == '0':
        break
    print(f'Is the password valid: {is_valid_password(input_pass)}')

TEXT = ("Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. "
        "Смешно, не не правда ли? Не нужно портить хор хоровод.")

print(errors_correction(TEXT))
