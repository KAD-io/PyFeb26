def is_win(player, field):
    win = player * 3
    for l in range(3):
        if field[l][0] + field[l][1] + field[l][2] == win:
            return True

    for r in range(3):
        if field[0][r] + field[1][r] + field[2][r] == win:
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
        l, r = map(int, input("Enter the coordinates separated by a space: ").split())
        if field[l][r] != ' ':
            print("Cage is occupied")
            continue

        field[l][r] = player
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