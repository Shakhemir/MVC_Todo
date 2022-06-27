def show_menu_commands(menu_list, light=False):
    menu = ' | '.join(menu_list)
    if not light:
        print()
        print('=' * len(menu))
    print(menu)
    if not light:
        print('=' * len(menu))
        print()


def select_menu():
    return input('Выберите номер команды (для выхода пустая строка): ')


def max_limit_input(max_limit: int, text=''):
    txt_len = max_limit + 1
    input_text = ''
    while txt_len > max_limit:
        input_text = input(text)
        txt_len = len(input_text)
        if txt_len > max_limit:
            print(f'Введите не больше {max_limit} символов (у вас {txt_len})')
    return input_text


def select_todo(todo_list, for_what=''):
    from show_list import show_todo_list
    show_todo_list(todo_list)
    max_id = len(todo_list)
    select_todo_id = '?'
    while not select_todo_id.isdigit() or int(select_todo_id) not in range(max_id):
        select_todo_id = input(f'Выберите N дела {for_what} (пустая строка - отмена): ')
        if select_todo_id == '':
            return False
    return int(select_todo_id)


def confirm_input(text=''):
    answer = input(f'{text} (для подтверждения введите "да"/"yes"/"y")?')
    return answer.lower() in ('да', 'yes', 'y')
