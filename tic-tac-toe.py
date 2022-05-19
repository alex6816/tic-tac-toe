def greet():  # Приветствие
    print('-----------------')
    print(' Приветствуем Вас')
    print('     в игре      ')
    print('крестики - нолики')
    print('-----------------')
    print('формат ввода: x y')
    print('x - номер строки ')
    print('y - номер столбца')
    print('-----------------')


def show():  # Рисуем поле для игры
    print()
    print('      0   1   2  ')
    print('    -------------')
    for i, row in enumerate(field):
        row_string = f' {i}  | {" | ".join(row)} |'
        print(row_string)
        print('    -------------')


def ask():          # Ввод пользователем координат его хода и
    while True:     # проверка введенных данных
        coords = input('      Ваш ход:  ').split()

        if len(coords) != 2:
            print('Введите две координаты!')
            continue

        x, y = coords

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Координаты вне диапазона!')
            continue

        if field[x][y] != ' ':
            print('Клетка занята! Выберите другую.')
            continue

        return x, y


def win_check():    # Определяем победителя
    win_point = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))

    for coords in win_point:
        chars = []

        for c in coords:
            chars.append(field[c[0]][c[1]])

        if chars == ['X', 'X', 'X']:
            print('Ура!!! Выиграл крестик!')
            return True
        if chars == ['0', '0', '0']:
            print('Ура!!! Выиграл нолик!')
            return True

    return False


greet()

field = [[' '] * 3 for i in range(3)]
num_move = 0           # Счетчик количества ходов

while True:
    num_move += 1

    show()

    if num_move % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask()

    if num_move % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if win_check():
        break

    if num_move == 9:
        print('Ничья!')
        break
