import random
def print_board(board_list):
    print(f"   |   |   ")
    print(f" {board_list[0]} | {board_list[1]} | {board_list[2]} ")
    print(f"   |   |   ")
    print(f"-----------")
    print(f"   |   |   ")
    print(f" {board_list[3]} | {board_list[4]} | {board_list[5]} ")
    print(f"   |   |   ")
    print(f"-----------")
    print(f"   |   |   ")
    print(f" {board_list[6]} | {board_list[7]} | {board_list[8]} ")
    print(f"   |   |   ")

def player_input(board_list,which_player):
    number = ""
    while number not in [str(i) for i in range(1,10)]:
        number = input("Choose your next position: (1-9)")
        if number not in [str(i) for i in range(1,10)]:
            print("Invalid input")
        elif board_list[int(number)-1] != " ":
            print("Invalid input")
        else:
            board_list[int(number)-1] = which_player

def check_winner(board_list):
    if (board_list[0] == board_list[1] == board_list[2]) and board_list[0] != " ":
        return True
    elif (board_list[3] == board_list[4] == board_list[5]) and board_list[3] != " ":
        return True
    elif (board_list[6] == board_list[7] == board_list[8]) and board_list[6] != " ":
        return True
    elif (board_list[0] == board_list[3] == board_list[6]) and board_list[0] != " ":
        return True
    elif (board_list[1] == board_list[4] == board_list[7]) and board_list[1] != " ":
        return True
    elif (board_list[2] == board_list[5] == board_list[8]) and board_list[2] != " ":
        return True
    elif (board_list[0] == board_list[4] == board_list[8]) and board_list[0] != " ":
        return True
    elif (board_list[2] == board_list[4] == board_list[6]) and board_list[2] != " ":
        return True
    else:
        return False

def play_on(board_list):
    play_again = ""
    for i in range(len(board_list)):
        board_list[i] = " "
    while play_again not in ["Yes", "No"]:
        play_again = input("Do you want to play again? (Yes/No)")
        if play_again not in ["Yes", "No"]:
            print("Invalid input")
        if play_again == "Yes":
            return True, board_list
        elif play_again == "No":
            return False, board_list

def player_icon():
    player1_icon = ""
    player2_icon = ""
    while player1_icon not in ["X", "O"]:
        player1_icon = input("Player 1: Do you want to be X or O")
        if player1_icon not in ["X", "O"]:
            print("Invalid input")
        if player1_icon == "X":
            return "X", "O"
        elif player1_icon == "O":
            return "O", "X"

def ready_to_play():
    ready_play = ""
    while ready_play not in ["Yes", "No"]:
        ready_play = input("Are you ready to play? (Yes/No)")
        if ready_play not in ["Yes", "No"]:
            print("Invalid input")
        if ready_play == "Yes":
            return True
        elif ready_play == "No":
            return False

if __name__ == '__main__':
    print("Welcome to Tik-Tac-Toe!")
    board = [" "," "," "," "," "," "," "," "," "]
    player1,player2 = player_icon()
    play = ready_to_play()
    while play:
        turn = random.randint(1,2)
        print(f"Player {turn} will go first.")
        while not check_winner(board):
            if " " not in board:
                break
            print_board(board)
            if turn == 1:
                player_input(board,player1)
                turn = 2
            else:
                player_input(board,player2)
                turn = 1
        if " " not in board and not check_winner(board):
            print_board(board)
            print("There is no winner.")
        else:
            print_board(board)
            if turn == 1:
                turn = 2
            else:
                turn = 1
            print(f"Congratulations! Player {turn} has won the game!")
        play, board = play_on(board)

#testest