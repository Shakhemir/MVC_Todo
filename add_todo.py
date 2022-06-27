from config import fields
import user_interface as ui


def new_todo(todo_list):
    new_todo = []
    for i, field in enumerate(fields[:-1]):
        new_field = ui.max_limit_input(field[1], f'{field[0]}: ')
        new_todo.append(new_field)
    new_todo.append('0')
    todo_list.append(new_todo)
    return todo_list
