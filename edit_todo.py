from config import fields
import user_interface as ui


def edit_todo(todo_list):
    edit_id = ui.select_todo(todo_list, 'для изменения')
    if edit_id:
        print(f'Введите новые значения для дела (пустая строка, чтобы оставить как есть):')
        for i, edit_field in enumerate(todo_list[edit_id][:-1]):
            print(f'{fields[i][0]} ({edit_field}):')
            new_field = ui.max_limit_input(fields[i][1])
            if new_field != '':
                todo_list[edit_id][i] = new_field
    return todo_list
