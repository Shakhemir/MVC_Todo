from config import log_file


def add_log(text):
    with open(log_file, 'a') as file:
        print(text, file=file)