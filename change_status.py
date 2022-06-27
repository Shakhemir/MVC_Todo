from config import menu_edit_status, fields
import user_interface as ui


def new_status(todo_list):
    change_id = ui.select_todo(todo_list, 'для изменения статуса или удаления')
    if change_id is not None:
        ui.show_menu_commands(menu_edit_status, light=True)
        select_command = ui.select_menu()
        if select_command.isdigit():
            select_command = int(select_command)
            if select_command == 1:
                todo_list[change_id][len(fields) - 1] = '1'
            elif select_command == 2:
                todo_list = delete_todo(todo_list, change_id)
    return todo_list


def delete_todo(todo_list, del_id):
    confirm = ui.confirm_input(f'Вы точно хотите удалить дело N {del_id} "{todo_list[del_id][0]}"')
    if confirm:
        deleted_todo = todo_list.pop(del_id)
        print(f'Дело N {del_id} "{deleted_todo[0]}" удалено!')
    return todo_list
