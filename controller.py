import user_interface as ui
import config
import show_list
import csv_io
import add_todo
import edit_todo
import change_status

todo_list = []


def run_app():
    init()
    main_polling()


def init():
    global todo_list
    todo_list = csv_io.read_data()


def main_polling():
    command = '?'
    while command != '':
        ui.show_menu_commands(config.menu)
        command = ui.select_menu()
        if command.isdigit():
            execute_command(int(command))
    shut_down()


def execute_command(command):
    global todo_list
    if command == 1:  # показать список дел
        show_list.show_todo_list(todo_list)
    elif command == 2:  # добавить дело
        todo_list = add_todo.new_todo(todo_list)
        csv_io.save_data(todo_list)
    elif command == 3:  # редактировать дело
        todo_list = edit_todo.edit_todo(todo_list)
        csv_io.save_data(todo_list)
    elif command == 4:  # изменить статус дела
        todo_list = change_status.new_status(todo_list)
        csv_io.save_data(todo_list)
    else:
        print("Введите верную команду")


def shut_down():
    pass
