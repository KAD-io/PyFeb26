def is_win(player, field):
    win = player * 3
    for col in range(3):
        if field[col][0] + field[col][1] + field[col][2] == win:
            return True

    for row in range(3):
        if field[0][row] + field[1][row] + field[2][row] == win:
            return True

    if field[0][0] + field[1][1] + field[2][2] == win:
        return True

    if field[0][2] + field[1][1] + field[2][0] == win:
        return True

    return False


def print_field(field):
    for line in field:
        print(line)


def test02_task08():
    field = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    player = "X"
    counter = 0

    while True:
        print_field(field)
        col, row = map(int, input("Enter the coordinates separated by a space: ").split())
        if field[col][row] != ' ':
            print("Cage is occupied")
            continue

        field[col][row] = player
        counter += 1

        if is_win(player, field):
            print_field(field)
            print(f"Winner: {player}!")
            break

        if counter == 9:
            print_field(field)
            print("Friendship has won :)")
            break

        player = "O" if player == "X" else "X"


test02_task08()