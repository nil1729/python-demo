# Welcome Message
print('-' * 10 + 'WELCOME TO  TIC-TAC-TOE !!' + '-' * 10)

# Board Configuration
print('This is  Input(1-9) format :')


# Show Table
def show_table(table, config=False):
    print('\n')
    for i in range(5):
        row = []
        if i % 2 == 0:
            for j in range(5):
                if j % 2 == 0:
                    char = table[(3 - i // 2) * 3 - (2 - (j // 2)) - 1]
                    if type(char) == int:
                        if config:
                            row.append(str(char))
                        else:
                            row.append(" ")
                    else:
                        row.append(char)
                else:
                    row.append('|')
            print('\t' * 3 + f"{''.join(row)}")
        else:
            print('\t' * 3 + '-' * 5)
    print('\n')


# Show Board Configuration
show_table(list(range(1, 10)), True)


# Game Options Choose (1-9)
def choose_option(**kwargs):
    def check_input(option):
        if len(option) == 1 and 49 <= ord(option) <= 57:
            return int(option)
        else:
            return choose_option(error=True, player=kwargs['player'])

    if 'error' in kwargs:
        if 'options' not in kwargs:
            print('Please enter a Number between 1 to 9')
            pass
        else:
            print('Available options:', kwargs['options'])
            return check_input(input('Player ' + f"{kwargs['player']}" + ' enter a available Choice: \t'))
    return check_input(input('Player ' + f"{kwargs['player']}" + ' Choose (1-9):\t'))


# Winner Check
def is_winner(table):
    cond1 = table[0] == table[4] == table[8] or table[6] == table[4] == table[2]
    cond2 = table[3] == table[4] == table[5] or table[0] == table[1] == table[2] or table[6] == table[7] == table[8]
    cond3 = table[6] == table[3] == table[0] or table[7] == table[4] == table[1] or table[8] == table[5] == table[2]

    if cond1 or cond2 or cond3:
        return True
    else:
        return False


# Global Variable
match = 1
score = [0, 0]


# Show Results
def show_result():
    print('\n'*2)
    print('\t' * 4 + 'Total Match:', match)
    print('\t' * 4 + 'Player 1 score:', score[0])
    print('\t' * 4 + 'Player 2 score:', score[1])
    print('\n' + '\t' * 4 + '-' * 7 + 'GAME___OVER' + '-' * 7 + '\n')


# Game Start
def game_start(**kwargs):
    innings = 0
    players = {1: kwargs['player1'], 2: kwargs['player2']}
    winner = None
    available_option = list(range(1, 10))
    table = list(range(1, 10))

    while innings < 9 and not winner:
        player = innings % 2 + 1
        option = choose_option(player=player)
        while option not in available_option:
            option = choose_option(player=player, options=available_option, error=True)
        else:
            index = available_option.index(option)
            available_option.pop(index)
            table[option - 1] = players[player]
            show_table(table)
            if not is_winner(table):
                innings += 1
                continue
            else:
                score[player - 1] += 1
                print('\t' * 4 + 'Winner is Player' + f'{player}')
                break
    if innings == 9:
        print('\t' * 4 + 'Match Tied')
    play_again = input('\nDo you want to play again? y/n\t')
    while play_again.lower() not in ['yes', 'y', 'no', 'n']:
        play_again = input('\nDo you want to play again? y/n\t')
    else:
        if play_again in ['yes', 'y']:
            global match
            match += 1
            return game(match)
        show_result()
        exit(200)


# Player 1 selection:
def show_option(e=False):
    if e:
        return input("Please enter a valid character ' X ' or ' O ' :\t")
    return input("Player 1: Do you want to be ' X ' or ' O ' ?\t")


def toss():
    chars = ['X', 'O']
    print('TOSS BETWEEN YOURSELVES and DECIDE WHO IS PLAYER 1')
    p1 = show_option()
    while p1 not in chars:
        p1 = show_option(True)
    else:
        p1 = chars.pop(chars.index(p1))
        p2 = chars[0]
        print('\n' + '-' * 7 + 'GAME___START' + '-' * 7 + '\n')
        game_start(player1=p1, player2=p2)


# Game Play
def game(times=1):
    print('\n' * 2 + '\t' * 4 + 'Match ' f'{times}' + '\n')
    toss()


game()
