# Welcome Message
print('----------WELCOME TO  TIC-TAC-TOE !!----------')

# Board Configuration
print('This is  Input(1-9) format :\n')


# Show Table
def show_table(table):
    print('\n')
    for i in range(5):
        row = []
        if (i % 2 == 0):
            for j in range(5):
                if (j % 2 == 0):
                    char = table[(3 - i // 2) * 3 - (2 - (j // 2)) - 1]
                    if (type(char) == int):
                        row.append(str(char))
                    else:
                        row.append(char)
                else:
                    row.append('|')
            print('\t' * 3 + f"{''.join(row)}")
        else:
            print('\t' * 3 + '-' * 5)
    print('\n')


# Show Board Configuration
show_table(list(range(1,10)))

# Game Options Choose (1-9)
def choose_option(**kwargs):
    if('error' in kwargs):
        print('Available options:', kwargs['options'])
        return int(input('Player ' + f"{kwargs['player']}" + ' enter a available Choice:'))
    return int(input('Player ' + f"{kwargs['player']}" + ' Choose (1-9): ' ))


# Winner Check
def is_winner(table):
    cond1 = table[0] == table[4] == table[8] or table[6] == table[4] == table[2]
    cond2 = table[3] == table[4] == table[5] or table[0] == table[1] == table[2] or table[6] == table[7] == table[8]
    cond3 = table[6] == table[3] == table[0] or table[7] == table[4] == table[1] or table[8] == table[5] == table[2]

    if(cond1 or cond2 or cond3):
        return True
    else:
        return False

# Game Start
def game_start(**kwargs):
    innings = 0
    players = {1:kwargs['player1'],2:kwargs['player2']}
    winner = None
    available_option = list(range(1, 10))
    table = list(range(1, 10))

    while(innings<9 and not winner):
        player = innings%2 + 1
        option = choose_option(player = player)
        while(option not in available_option):
            option = choose_option(player = player, options=available_option, error=True)
        else:
            index = available_option.index(option)
            available_option.pop(index)
            table[option-1] = players[player]
            show_table(table)
            if(not is_winner(table)):
                innings += 1
                continue
            else:
                print('Winner is Player' + f'{player}')
                break

# Player 1 selection:
def show_option(e=False):
    if(e):
        return input("Please enter a valid character 'X' or 'O'")
    return input("Player 1: Do you want to be ' X ' or ' O ' ?")

def toss():
    chars = ['X', 'O']
    print('TOSS BETWEEN YOURSELVES and DECIDE WHO IS PLAYER 1\n')
    p1 = show_option()
    while(p1 not in chars):
        p1 = show_option(True)
    else:
        p1 = chars.pop(chars.index(p1))
        p2 = chars[0]
        print('-'*7 + 'GAME___START' + '-'*7)
        game_start(player1 = p1, player2 = p2)
toss()