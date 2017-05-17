# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:48:37 2017

@author: PULKIT LUTHRA
"""

#Tic Tac Toe Game
import random
board=[]
for i in range(9):
    board.append(-1)

def drawBoard():
    print('     |      |')
    print(' ' + str(board[0]) + '  | ' + str(board[1]) + '   | ' + str(board[2]))
    print('     |      |')
    print('---------------')
    print('     |      |')
    print(' ' + str(board[3]) + '  | ' + str(board[4]) + '   | ' + str(board[5]))
    print('     |      |')
    print('---------------')
    print('     |      |')
    print(' ' + str(board[6]) + '  | ' + str(board[7]) + '   | ' + str(board[8]))
    print('     |      |')

def inputPlayerLetter():
    letter = input("Do you want to be X or O?")
    letter=letter.upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def checkWinner(bo, le):
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or 
    (bo[3] == le and bo[4] == le and bo[5] == le) or 
    (bo[0] == le and bo[1] == le and bo[2] == le) or 
    (bo[6] == le and bo[3] == le and bo[0] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[6] == le and bo[4] == le and bo[2] == le) or 
    (bo[8] == le and bo[4] == le and bo[0] == le))   

def getPlayerMove(playerLetter):
    while True:
        move = input("What is your next move? (0-8)")
        move=int(move)
        if board[move]!=-1:
            print ('Invalid move! Cell already taken. Please try again.\n')
        else:
            board[move]=playerLetter
            return

def getComputerMove(computerLetter):
    while True:
        move = int(random.randint(0,8))
        if board[move]!=-1:
            #print ('Invalid move! Cell already taken. Please try again.\n')
            continue
        else:
            board[move]=computerLetter
            return 
    
drawBoard()    
playerLetter, computerLetter = inputPlayerLetter()
turn = whoGoesFirst()
print('The ' + turn + ' will go first.')
count=0
while True:
    #xprint ()
    #print (count)
    if turn=='player':
       count+=1
       getPlayerMove(playerLetter)
       drawBoard()
       if count>=5:
           if checkWinner(board,playerLetter):
               print ("Hurray!!!!You Win")
               break
       if count==9:
           print ("The match is drawn")
           break

       turn = 'computer'
    else:
        print ('Computers Turn')
        count+=1
        
        getComputerMove(computerLetter)
        drawBoard()
        if count>=5:
           if checkWinner(board,computerLetter):
               print ("You Lose")
               break
        if count==9:
           print ("The match is drawn")
           break

        turn = 'player'
    
