import numpy as np


def change_mark(mark):
    if mark == 'x':
        return 'o'
    else:
        return 'x'


def beautify_print(field):
    head = [" ", 0, 1, 2]
    print(*head)
    for i in range(3):
        print(head[i+1], *field[i])


def check_unique(flat_array):
    if np.any(flat_array == 'x') or np.any(flat_array == 'o'):
        return np.all(flat_array == flat_array[0])


def get_winner(field):
    rows = []
    columns = []
    for i in range(len(field)):
        rows.append(field[i, :])
        columns.append(field[:, i])

    for row in rows:
        if check_unique(row):
            return row[0]

    for column in columns:
        if check_unique(column):
            return column[0]

    flipped_field = np.flipud(field)
    diagonals = [flipped_field.diagonal(), field.diagonal()]

    for diagonal in diagonals:
        if check_unique(diagonal):
            return diagonal[0]

    return None


desk = np.full((3, 3), '-')
beautify_print(desk)
end_of_game = False
mark = "x"
winner = None

while not end_of_game:
    print("Turn ", mark)
    accept = False
    while not accept:
        row = int(input("Input row index [0, 2]: "))
        col = int(input("Input column index [0, 2]: "))
        if desk[row][col] == '-':
            accept = True
        elif row < 0 or row > 2 or col < 0 or col > 2:
            print("Choose valid cell")
        else:
            print("Choose empty cell")

    desk[row][col] = mark
    beautify_print(desk)
    print()
    mark = change_mark(mark)

    winner = get_winner(desk)
    if winner is not None:
        end_of_game = True

if winner == 'x':
    print()
    print("x win")
elif winner == 'o':
    print()
    print("o win")
else:
    print()
    print("Tie")