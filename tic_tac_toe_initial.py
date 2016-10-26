import os

def main():
    global menu_decision
    global board
    global move_count
    global winner
    clear_screen()
    board = [' '] * 9
    move_count = -1
    winner = ' '
    print_menu()
    menu_decision = process_menu_decision()
        
def clear_screen():
    clear = os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print('--- TIC TAC TOE ---\n')
    print('  Welcome friend!\n')
    print('1. Play')
    print('2. Quit\n')

def process_menu_decision():
    menu_user_input = ""
    while menu_user_input not in ['1', '2']:
        menu_user_input = input('Enter a number (1 or 2): ')
    if '1' == menu_user_input:
        choosen_mark_check()
        print_instruction()
        game()
        return 1
    if '2' == menu_user_input:
        print('What a pity!')
    return 2

def choosen_mark_check():
    global playerX
    global playerO
    while True: 
        choosen_mark = input('Enter the mark what you\'ve choosen (X/O): ')
        if choosen_mark == 'X' or choosen_mark == 'x':
            playerX = '\033[1;36mX\033[1;m'
            playerO = '\033[1;33mO\033[1;m'
            player_name_input()
            break
        elif choosen_mark == 'O' or choosen_mark == 'o':
            playerX = '\033[1;33mO\033[1;m'
            playerO = '\033[1;36mX\033[1;m'
            player_name_input()
            break
        else: 
            ValueError()

def player_name_input():
    global first_player_name
    global second_player_name
    first_player_name = input('Please enter your name: ')
    second_player_name = input('Please enter your name: ')
    clear_screen()

def print_instruction():
	print('You can use the folling numbers to make your move:\n')
	print_board([1,2,3,4,5,6,7,8,9])

def print_board(board):
    for i in range(3):
        print(' ', end='')
        for j in range(3):
            if -1 < move_count:
                print_marks_in_board(board, i, j)
            #print board with instruction numbers
            else:
                print(board[i*3+j], end='') 
            #print walls
            if j != 2:
                print(' | ', end='')
        #print walls
        if i != 2:
            print('\n''-----------')
    print('\n')

def print_marks_in_board(board, i, j):
    if board[i*3+j] == 1:
        print(playerX, end='')
    elif board[i*3+j] == 0:
        print(playerO, end='')
    else: 
        print(' ', end='')

def game():
    global move_count
    while True:
        no_more_step(board)
        check_win(board)
        move_count += 1
        player_turn_counter()

def no_more_step(board):
    if board.count(' ') == 0:
        print('There is no winner.')
        restart_f()

# win and winner check functions
def check_win(board):
    if board[0] == board[1] and board[0] == board[2] and board[0] != (' '):
        who_the_winner_0(board)
    if board[4] == board[3] and board[4] == board[5] and board[4] != (' '):
        who_the_winner_4(board)
    if board[8] == board[7] and board[8] == board[6] and board[8] != (' '):
        who_the_winner_8(board)
    if board[0] == board[3] and board[0] == board[6] and board[0] != (' '):
        who_the_winner_0(board)
    if board[4] == board[1] and board[4] == board[7] and board[4] != (' '):
        who_the_winner_4(board)
    if board[8] == board[5] and board[8] == board[2] and board[8] != (' '):
        who_the_winner_8(board)
    if board[0] == board[4] and board[0] == board[8] and board[0] != (' '):
       who_the_winner_0(board)
    if board[4] == board[2] and board[4] == board[6] and board[4] != (' '):
        who_the_winner_4(board)

def who_the_winner_0(board):
    global winner
    if board[0] == 0:
        winner = playerO
    elif board[0] == 1:    
        winner = playerX
    winner_script(winner)

def who_the_winner_4(board):
    global winner
    if board[4] == 0:
        winner = playerO
    elif board[4] == 1:    
        winner = playerX
    winner_script(winner)

def who_the_winner_8(board):
    global winner
    if board[8] == 0:
        winner = playerO
    elif board[8] == 1:    
        winner = playerX
    winner_script(winner)

def winner_script(winner):
    if winner == playerO and playerO == '\033[1;36mX\033[1;m':
        print('\033[1;36mThe winner is X\033[1;m')
        
    elif winner == playerX and playerX == '\033[1;36mX\033[1;m':
        print('\033[1;36mThe winner is X\033[1;m')
    
    elif winner == playerO and playerO == '\033[1;33mO\033[1;m':
        print('\033[1;33mThe winner is O\033[1;m')

    elif winner == playerX and playerX == '\033[1;33mO\033[1;m':
        print('\033[1;33mThe winner is O\033[1;m')
    restart_f()

def player_turn_counter():
    if move_count % 2 == 0:
        player_mark = playerX
        player_name = first_player_name
    else: 
        player_mark = playerO
        player_name = second_player_name
    player_input = user_input(player_mark, player_name)

    if player_mark == playerX:
        board[player_input] = 1
    else:
        board[player_input] = 0
    print_board(board)

# provide input from user, input check AND exit condition
def user_input(player_mark, player_name):
    while True: 
        try: 
            print('You can quit anytime by type the exit command!')
            player_input = input(player_name + ' - Where would you ' +
                        'like to place the ' + player_mark + ' mark(1-9)? ')
            print('\n')
            if player_input == 'exit':
                quit()
            player_input = int(player_input)
            if player_input >=1 and player_input <= 9 and board[player_input -1] == ' ':
                return player_input -1
            else: 
                print('\n\033[1;31mThat is not a valid move, please try again.\033[1;m\n')
        except Exception as e:
            print('\033[1;31mThis is not a valid move, please try again.\033[1;m\n')

def restart_f():
    global menu_decision
    start_again = input('If you want to start again type y? \n')    
    if start_again == 'y':
        main()
    else:
        quit()

main()