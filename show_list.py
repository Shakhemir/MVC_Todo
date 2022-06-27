from config import fields, todo_status


def show_todo_list(todo_list):
    width = sum([f[1] for f in fields]) + len(fields) * 2  # ширина записи дела
    print('-' * width)
    size = len(str(len(todo_list)))  # узнаем какого размера должен быть id контакта для выравнивания
    print(f'{"N".ljust(size)}  {"  ".join([f[0].ljust(f[1]) for f in fields])}')
    print('-' * width)
    for id, todo in enumerate(todo_list):
        print(str(id).zfill(size), end='  ')
        for i, element in enumerate(fields):
            if i != len(fields) - 1:
                print(todo[i].ljust(element[1]), end='  ')
            else:
                print(todo_status[int(todo[i])], end='')
        print()
    print('-' * width)
