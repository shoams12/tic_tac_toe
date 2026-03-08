import time


def create_board() -> list:
    return ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']


def print_board(board: list) -> None:
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        print("----+----+--- ")


def print_cur_player(player: str) -> None:
    print(f"Now playing: {player}")


def get_move(player: str, board: list) -> int:
    # handle 1-9 and taken spot
    while True:
        player_place = input(f"Enter 1-9 to place your {player}: ")
        if not player_place.isdigit() or not int(player_place) in range(1, 10):
            print("Invalid input")
            continue
        elif board[int(player_place)-1] != '  ':
            print("This place is already taken")
            continue

        break
    return int(player_place)


def make_move(board: list, position: int, symbol: str) -> None:
    board[position-1] = symbol


def check_winner(board: list, symbol: str) -> bool:

    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == symbol:
            return True

    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == symbol:
            return True

    # check diagonals
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True

    return False


def is_tie(board: list) -> bool:
    return all(place != '  ' for place in board)


def switch_player(current: str) -> str:
    return '✖️' if current == '⭕' else '⭕'


def play_game() -> None:
    my_board = create_board()
    cur_player = '⭕'
    while True:
        print_board(my_board)
        print_cur_player(cur_player)
        player_move = get_move(cur_player, my_board)
        make_move(my_board, player_move, cur_player)
        if check_winner(my_board, cur_player):
            print_board(my_board)
            print(f"Player {cur_player} is the winner🏆")
            break
        elif is_tie(my_board):
            print_board(my_board)
            print("Tie🤜🏽🤛🏽")
            break
        cur_player = switch_player(cur_player)

    play_again = input("Play again? (y/n)")
    if play_again == 'y':
        print("Game starts")
        time.sleep(2)
        play_game()
    return


play_game()
