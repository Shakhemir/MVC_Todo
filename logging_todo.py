from config import log_file
from datetime import datetime


def add_log(text):
    with open(log_file, 'a') as file:
        print(f'{datetime.now().strftime("%Y.%m.%d %H:%M:%S")} {text}', file=file)