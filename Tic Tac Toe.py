# These are the libraries that I used in my code:
import random #this is used to generate random numbers for moves of the AI

symbol = input("Choose X or O: ").capitalize()
symbol = symbol.strip()
print('You chose ' + symbol)

states = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
winconditions = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]
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
    if character == symbol:
        move = input('Choose a location for your move (one of the numbers): ')
        move = int(move.strip())
        states[move-1] = character
    else:
        picked = False
        while picked == False:
            move = random.randint(0, 8)
            if states[move] != 'O' and states[move] != 'X':
                states[move] = character
                picked = True
            else:
                continue

printboard(states)
states = ['.', '.', '.', '.', '.', '.', '.', '.', '.']


while True:
    print("X turn")
    move('X')
    printboard(states)

    print("O turn")
    move('O')
    printboard(states)

    for wincondition in winconditions:
        winchecker = states[wincondition[0]] + states[wincondition[1]] + states[wincondition[2]]
        if winchecker == "XXX":
            print('X wins!')
            quit()
        elif winchecker == "OOO":
            print("O wins")
            quit()
