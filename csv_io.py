from config import csv_file
from os.path import exists


def read_data():
    todo_list = []
    if exists(csv_file):
        with open(csv_file, 'r') as file:
            for contact_line in file.readlines():
                contact = contact_line.strip().split(';')
                todo_list.append(contact)
    return todo_list


def save_data(todo_list: list):
    with open(csv_file, 'w') as file:
        for contact in todo_list:
            print(';'.join(contact), file=file)
