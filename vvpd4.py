menu = ['Введите команду из списка ниже: ', '0 - Выход',
        '1 - Вывод должников', '2 - Оценка', ]

import datetime as dt


def valid_date(date):
    try:
        dt.datetime(*tuple(map(int, date.split('.')[::-1])))
    except ValueError:
        raise ValueError


def late_list(dct, deadline):
    dct_debtors = dict()
    for name_st, date in dct.items():
        mark = deadline_score(date, deadline)
        if mark < 5:
            dct_debtors[name_st] = date
    return list(dct_debtors.keys())


def deadline_score(date, deadline):
    deadline = dt.datetime(*tuple(map(int, deadline.split('.')[::-1])))
    date = dt.datetime(*tuple(map(int, date.split('.')[::-1])))
    mark = 5
    if 14 > (date - deadline).days > 7:
        mark = mark - 1
    elif 21 > (date - deadline).days > 14:
        mark = mark - 2
    elif 28 > (date - deadline).days > 21:
        mark = mark - 3
    elif 35 > (date - deadline).days > 28:
        mark = mark - 4
    elif (date - deadline).days > 35:
        mark = mark - 5
    return mark


dl = input('Дата дедлайна: ')
valid_date(dl)
data = dict()
while True:
    name = input('Имя студента: ')
    if name == "stop":
        break
    date_sd = input('Дата сдачи работы: ')
    valid_date(dl)
    data[name] = date_sd

while True:
    print('\n'.join(menu))
    command = input()
    if command == '0':
        break
    elif command == '1':
        lst = late_list(data, dl)
        print(*lst, sep="\n")
    elif command == '2':
        student_name = input("Чью оценку узнаём? ")
        print(deadline_score(data[student_name], dl))
    else:
        print('Ошибка ввода')
