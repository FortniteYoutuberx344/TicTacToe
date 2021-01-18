# These are the libraries that I used in my code:
import random #this is used to generate random numbers for moves of the AI

symbol = input("Choose X or O: ").capitalize()
symbol = symbol.strip()
print('You chose ' + symbol)
states = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def printboard(state):
    print('---')
    boardline=''
    for tile in range(len(state)):
        boardline += state[tile]
        if (tile + 1) % 3 == 0:
            print(boardline)
            boardline = ''
    print('---')

def move(character):
    if character == 'X':
        move = input('Choose a location for your move (one of the numbers): ')
        move = int(move.strip())
        states[move-1] = 'X'
    else:
        picked = False
        while picked == False:
            move = random.randint(0, 8)
            if states[move] != 'O' and states[move] != 'X':
                states[move] = 'X'
                picked = True
            else:
                continue
    if character == 'O':
        move = input('Choose a location for your move (one of the numbers): ')
        move = int(move.strip())
        states[move-1] = 'O'
    else:
        picked = False
        while picked == False:
            move = random.randint(0, 8)
            if states[move] != 'O' and states[move] != 'X':
                states[move] = 'O'
                picked = True
            else:
                continue

printboard(states)
states = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

won = False

while won == False:

    print("X turn")
    if symbol == 'X':
        move('X')
    printboard(states)

    print("O turn")
    if symbol == 'O':
        move('O')
    printboard(states)
