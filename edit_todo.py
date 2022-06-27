from config import fields
import user_interface as ui
from logging_todo import add_log


def edit_todo(todo_list):
    edit_id = ui.select_todo(todo_list, 'для изменения')
    if edit_id is not None:
        log_changes = f'Edit_todo: {todo_list[edit_id]} changes: '
        ui.my_print(f'Введите новые значения для дела (пустая строка, чтобы оставить как есть):')
        for i, edit_field in enumerate(todo_list[edit_id][:-1]):
            print(f'{fields[i][0]} ({edit_field}):')  # Вывод названия поля (в скобках старое значение)
            new_field = ui.max_limit_input(fields[i][1])  # ввод нового значения поля с лимитом
            if new_field != '':  # если пользователь ввел пустую строку, то оставляем старое значение
                todo_list[edit_id][i] = new_field
                log_changes += f'{fields[i][0]}: {new_field} '
        add_log(log_changes)
    return todo_list
