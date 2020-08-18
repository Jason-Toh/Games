#Name: Jason Toh Zhern Wee
#Student ID: 29798183
import copy

def new_board():
    board=[[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,2,1,0,0,0],
           [0,0,0,1,2,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]
    return board

def score(board):
    s1=0
    s2=0

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]==1:#Player's one score
                s1 = s1 + 1
            elif board[y][x]==2:#Player's two score
                s2 = s2 + 1
    return(s1,s2)

def print_board(board):
    n=0
    ASCII_a=97#Value of a in ASCII table
    for y in range(len(board)):
        n = n + 1
        print(n,sep='',end=' |')#sep separates the elements and each elements end a vertical line
        for x in range(len(board[y])):
            if board[y][x] == 0:
                printString = '   '
            elif board[y][x] == 1:
                printString = ' B '
            elif board[y][x] == 2:
                printString = ' W '
            print(printString,sep='',end='|')
        print("\n",("--")*18,sep='')
    print('  |', end = '')

    for y in range(len(board)):
        alphabets= y + ASCII_a
        print(chr(alphabets),sep='',end='  |')#This will convert the value into character form
    print('\n\n', end = '')

def enclosing(board,player,pos,direct):
    y, x = pos
    direct_y, direct_x = direct
    translate_y = y + direct_y
    translate_x = x + direct_x
    users=(1,2)

    while player in users:
        if player==1:
            if (translate_y)>=8 or (translate_x)>=8 or (translate_y)<0 or (translate_x)<0:#To check whether its out of range after translation
                return False
            
            if board[translate_y][translate_x]!=player and board[translate_y][translate_x]!=0:#Checks if any of the position is the next player's piece
                newpos=(translate_y,translate_x)#If True, then the position will switch to that spott
                return enclosing(board,player,newpos,direct)#Call the function until you either find your own piece or an empty spot
            
            elif board[y][x]!= player and board[y][x] != 0 and board[translate_y][translate_x] == player:
                return True#If the current position is not your piece nor an empty spot and the position next to the current position is your own piece, return True
            
            else:#Return false when the position you want to enclose is an empty spot or your own stone
                return False
        
        elif player==2:
            if (translate_y)>=8 or (translate_x)>=8 or (translate_y)<0 or (translate_x)<0:
                return False
            
            if board[translate_y][translate_x]!=player and board[translate_y][translate_x]!=0:
                newpos=(translate_y,translate_x)
                return enclosing(board,player,newpos,direct)
            
            elif board[y][x]!= player and board[y][x] != 0 and board[translate_y][translate_x] == player:
                return True
            
            else:
                return False

def valid_moves(board,player):
    possible_moves=[]
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]==0:#If the position is an empty spot
                for direct_y in range(-1,2):#This will loop through all possible moves(-1,0,1)
                    for direct_x in range(-1,2):
                        if enclosing(board,player,(y,x),(direct_y,direct_x))==True:
                            possible_moves.append((y,x))
    return possible_moves

def flip(board, player, pos, direct):#This function is used to flip all the stones
    y, x = pos
    direct_y, direct_x = direct
    translate_y = y + direct_y
    translate_x = x + direct_x
    users=(1,2)

    while player in users:
        if player==1:
            if (translate_y)>=8 or (translate_x)>=8 or (translate_y)<0 or (translate_x)<0:
                return None
          
            if board[translate_y][translate_x]!= player and board[translate_y][translate_x]!= 0:
                newpos = (translate_y, translate_x)
                board[translate_y][translate_x]=player#Flips all the stones
                if board[translate_y][translate_x]==player:
                    board[y][x]=player#The translated position becomes the current player's piece
                return flip(board, player, newpos, direct)
            
            else:
                return board
        elif player==2:
            if (translate_y)>=8 or (translate_x)>=8 or (translate_y)<0 or (translate_x)<0:
                return None
          
            if board[translate_y][translate_x]!= player and board[translate_y][translate_x]!= 0:
                newpos = (translate_y, translate_x)
                board[translate_y][translate_x] = player
                if board[translate_y][translate_x]==player:
                    board[y][x]=player
                return flip(board, player, newpos, direct)
            
            else:
                return board

def next_state(board,player,pos):
    y, x=pos
    users=(1,2)

    while player in users:
        if player==1:
            for direct_x in range (-1, 2):
                for direct_y in range (-1, 2):
                    if enclosing(board, player, pos, (direct_y,direct_x)):
                        flip(board, player, pos, (direct_y,direct_x))
            if valid_moves(board,1)==[] and valid_moves(board,2)==[]:
                return(board,0)#If both players have no more moves, game ends
            elif valid_moves(board,2)==[]:
                return (board,1)#If player 2 have no more moves, switch to player 1
            else:
                return(board,2)#If player 1 have no more moves, switch to player 2
            
        elif player==2:
            for direct_x in range (-1, 2):
                for direct_y in range (-1, 2):
                    if enclosing(board, player, pos, (direct_y,direct_x)):
                        flip(board, player, pos, (direct_y,direct_x))
            if valid_moves(board,1)==[] and valid_moves(board,2)==[]:
                return(board,0)
            elif valid_moves(board,1)==[]:
                return (board,2)
            else:
                return(board,1)

def position(string):
    string=string.lower()
    if len(string)!=2 or ord(string[0])<97 or ord(string[0])>104 or ord(string[1])>56 or ord(string[1])<49:#short circuit will occur at the len(string)!=2
        return None

    else:
        return(ord(string[1])-49,ord(string[0])-97)

def run_two_players():
    board = new_board()
    users=(1,2)
    player=1
    while True:
        print_board(board)
        print("Player's " + str(player) + " turn now")
        user_input=input("Please enter your move or press 'q' to quit: ")   
        if user_input=="q":
            break 
        pos=position(user_input)
        moves=valid_moves(board,player)
        while True:
            if pos == None or pos not in moves:
                print("Player's " + str(player) + " turn now")
                user_input=input("Invalid move, please enter again: ")
                pos=position(user_input)
            else:
                break
        board=next_state(board,player,pos)[0]
        player=next_state(board,player,pos)[1]
        if player == 0:
            if score(board)[0] > score(board)[1]: 
                print("Player " + str(users[0])+" has won! \nPlayer " + str(users[0]) + " has more stones than Player " + str(users[1]))
                print("Player " + str(users[0]) + "'s stones: " + str(score(board)[0]))
                print("Player " + str(users[1]) + "'s stones: " + str(score(board)[1]))
            elif score(board)[0] == score(board)[1]:
                print("Draw! Both players have same amount of stones")
                print("Player " + str(users[0]) + "'s stones: " + str(score(board)[0]))
                print("Player " + str(users[1]) + "'s stones: " + str(score(board)[1]))
            else:
                print("Player " + str(users[1])+" has won! \nPlayer " + str(users[1]) + " has more stones than Player " + str(users[0]))
                print("Player " + str(users[0]) + "'s stones: " + str(score(board)[0]))
                print("Player " + str(users[1]) + "'s stones: " + str(score(board)[1]))
            break

def run_single_player():
    board = new_board()
    users=(1,2)
    player=1
    while True:
        if player==1:  
            print_board(board)
            print("Player's " + str(player) + " turn now")
            user_input=input("Please enter your move or press 'q' to quit: ")
            if user_input=="q":
                break 
            pos=position(user_input)
            moves=valid_moves(board,player)
            while True:
                if pos == None or pos not in moves:
                    print("Player's " + str(player) + " turn now")
                    user_input=input("Invalid move, please enter again: ")
                    pos=position(user_input)
                else:
                    break
        elif player==2:
            print_board(board)
            scorecomp=0
            compmove=None
            nextboard=new_board()
            moves=valid_moves(board,player)

            for pos in moves:
                for direct_y in range(-1,2):
                    for direct_x in range(-1,2):
                        nextboard=copy.deepcopy(board)
                        y, x=pos
                        nextboard[y][x]=player
                        if enclosing(nextboard, player, pos, (direct_y,direct_x)):
                            testBoard = flip(nextboard, player, pos, (direct_y,direct_x))
                            
            if score(nextboard)[1] > scorecomp:#The computer will choose the move that can flip the most stones
                scorecomp = score(nextboard)[1]
                compmove = pos

        board=next_state(board,player,pos)[0]
        player=next_state(board,player,pos)[1]
        if player ==0:
            if score(board)[0] > score(board)[1]: 
                print("Player " + str(users[0])+" has won! \nPlayer " + str(users[0]) + " has more stones than Player " + str(users[1]))
                print("Player " + str(users[0]) + "'s stones: " + str(score(board)[0]))
                print("Player " + str(users[1]) + "'s stones: " + str(score(board)[1]))
            elif score(board)[0] == score(board)[1]:
                print("Draw! Both players have same amount of stones")
                print("Player " + str(users[0]) + "'s stones: " + str(score(board)[0]))
                print("Player " + str(users[1]) + "'s stones: " + str(score(board)[1]))
            else:
                print("Player " + str(users[1])+" has won! \nPlayer " + str(users[1]) + " has more stones than Player " + str(users[0]))
                print("Player " + str(users[0]) + "'s stones: " + str(score(board)[0]))
                print("Player " + str(users[1]) + "'s stones: " + str(score(board)[1]))
            break

def reversi():
    print("Welcome to R E S E R V I")

    while True:
        board=new_board()
        choice = str(input("You have two choices, \npress 1 to play against the computer or \npress 2 to play against another player: "))

        if choice=="1":
            run_single_player()
            break
        elif choice=="2":
            run_two_players()
            break
        else:
            print("Please enter 1 or 2")
                     
reversi()
