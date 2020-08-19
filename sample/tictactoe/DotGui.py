# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:01:07 2019

@author: umer
"""
#import os
#os.chdir('C:/Users/umer/Desktop/AdversarialSearchLab')
import pygame
import sys

from com.ai.adversarial.sample.tictactoe.tictactoeGame import TicTacToeGame
from pygame import gfxdraw
from com.ai.adversarial.search.simpleMinimax import SimpleMinimax
from com.ai.adversarial.search.alphaBetaMinimax import AlphaBetaMinimax



class dotGui(object):
    
    
    
    def __init__(self,width=500,height=500):
        
        self.gamm=TicTacToeGame()
        pygame.init()
        pygame.font.init()
        self.SURF=pygame.display.set_mode((width,height))
        pygame.display.set_caption("Brick Builder")
        self.myfont = pygame.font.SysFont('Arial', 50)
        self.score_font = pygame.font.SysFont('Arial', 30)
        self.dot_font = pygame.font.SysFont('Arial', 15)
        self.state = self.gamm.getInitialState()
        sys.setrecursionlimit(100000)
        self.score=[0,0]
        self.minimax = SimpleMinimax(self.gamm)
        self.SURF.fill((255, 255, 255))
        self.disp_board()
        self.cost = 4
        pygame.display.update()
        
        
    def disp_board(self):
        score = [0, 0] 
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        self.Black = (0, 0, 0)

       
        for i, point in enumerate(self.gamm.board):

            gfxdraw.filled_circle(self.SURF, point.x, point.y, 5, self.Black)
            gfxdraw.aacircle(self.SURF, point.x, point.y, 5, self.Black)
            dot_num = self.dot_font.render(str(i), True, self.Black)
            self.SURF.blit(dot_num, (point.x + 10, point.y - 20))
        
        if len(self.gamm.moves_done)>0 :
            for  move in self.gamm.moves_done:
                p1 = self.gamm.board[self.gamm.id_to_index(move.partners[0])]
                p2 = self.gamm.board[self.gamm.id_to_index(move.partners[1])]
                thickness = 3
                if move.O == "X":
                    pygame.draw.line(self.SURF, BLUE, (p1.x, p1.y), (p2.x, p2.y), thickness)
                elif move.O == "O":
                     pygame.draw.line(self.SURF, RED, (p1.x, p1.y), (p2.x, p2.y), thickness)
            
            pygame.display.update()
            



        
    def Algorithum(self):

            if len(self.gamm.moves_done) > 4:
                #print("len:{},cost:{}".format(len(self.gamm.moves_done),self.cost))
                self.cost +=1

            self.minimax.minimax_decision(self.state,self.cost )


            self.gamm.board[self.state._action[0]].partners.append(self.state._action[1])
            self.gamm.board[self.state._action[1]].partners.append(self.state._action[0])

            self.gamm.moves_done.append(self.gamm.move_Done((self.state._action[0], self.state._action[1]), 'O'))
            if self.complete():
                self.score[1] += 1
                self.disp_board()
                self.comp()
                self.Algorithum()






            self.state._move = 0
            self.state._utility = 0


    def complete(self):

        winposfound = True
        for i, pos in enumerate(self.gamm.boxes):
            winposfound = True
            if pos[4] == 0:
                for indpos in pos[:-1]:
                    if self.gamm.board[self.gamm.id_to_index(indpos[0])].id not in self.gamm.board[
                        self.gamm.id_to_index(indpos[1])].partners and self.gamm.board[
                        self.gamm.id_to_index(indpos[1])].id not in self.gamm.board[
                        self.gamm.id_to_index(indpos[0])].partners:
                        winposfound = False

                if winposfound:
                    self.gamm.boxes[i][4] = 1
                    return winposfound
                    break


        return winposfound


    def comp(self):
        if len(self.gamm.getActions(self.state))==0:
                if self.score[0] > self.score[1]:
                    print("You won! Score: {} to {}".format(self.score[0], self.score[1]))
                    input("Press enter to end game:")
                    pygame.quit()
                    sys.exit()
                elif call.score[1] > call.score[0]:
                    print("Computer won :( Score: {} to {}".format(self.score[0], self.score[1]))
                    input("Press enter to end game:")
                    pygame.quit()
                    sys.exit()
                else:
                    print("Tie game. Score: {} to {}".format(self.score[0], self.score[1]))
                    input("Press enter to end game:")
                    pygame.quit()
                    sys.exit()
        else:
            print("User Score: {} ,AI Score {}".format(self.score[0], self.score[1]))
    def user_move(self):
        try:
            p1,p2 = map(int,input("What move do you want to make?").split(","))
        except ValueError:
            print("Invalid move.")
            self.user_move()
        else:
            if self.gamm.is_connection(p1,p2):
                print("Sorry this move is already taken")
                self.user_move()
            elif not self.gamm.is_valid(p1,p2):
                print("Invalid move.")
                self.user_move()
            else:

                self.gamm.moves_done.append(self.gamm.move_Done((p1,p2),'X'))
                self.gamm.board[p1].partners.append(p2)
                self.gamm.board[p2].partners.append(p1)
                print('your move is Correct !now you have an other move!!')
                if self.complete():
                    self.score[0] += 1
                    self.disp_board()
                    self.comp()
                    self.user_move()

                self.state._move = 1

        
        
        
        

if __name__ == "__main__":

    call=dotGui()
    while True:




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        call.user_move()
        call.disp_board()
        call.Algorithum()
        call.disp_board()

