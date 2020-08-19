'''
Created on Mar 25, 2019

@author: dr.aarij
'''
#import os
#os.chdir('C:/Users/umer/Desktop/AdversarialSearchLab')
from com.ai.adversarial.sample.tictactoe.tictactoeState import TictactoeState
from com.ai.adversarial.sample.tictactoe.dotPlayer import DotPlayer
from com.ai.adversarial.elements.game import Game
from com.ai.adversarial.search.simpleMinimax import SimpleMinimax
from collections import namedtuple





class TicTacToeGame(Game):
    '''
    classdocs
    '''


    def __init__(self, move = 0):
        self.BOARDSIZE=4

        self.Point = namedtuple('Point', ['id', 'x', 'y', 'partners'])
        self.move_Done = namedtuple('move_Done', ['partners','O'])
        self.board = []
        for i in range(4):
            for i2 in range(4):

                self.board.append( self.Point(4 * i + i2, i2 * 100 + 100, i * 100 + 100, []))

        self._move = move
        self._agents =[ DotPlayer("Player","X"),
                       DotPlayer("Opponent","O")]
        
       # self._winningPositions = [[(0,0),(0,1),(0,2)],
         #                         [(1,0),(1,1),(1,2)],
          #                        [(2,0),(2,1),(2,2)],
           #                       [(0,0),(1,0),(2,0)],
            #                      [(0,1),(1,1),(2,1)],
             #                     [(0,2),(1,2),(2,2)],
              #                    [(0,0),(1,1),(2,2)],
               #                   [(2,0),(1,1),(0,2)]]

        self.moves_done=[]
        self.player = []
        
        self.boxes = [[(i, i+1),(i,i+self.BOARDSIZE),(i+1,i+self.BOARDSIZE+1), (i+self.BOARDSIZE,i+self.BOARDSIZE+1),0] for i in range(0,3)]
        self.boxes.extend([[(i, i+1),(i,i+self.BOARDSIZE),(i+1,i+self.BOARDSIZE+1), (i+self.BOARDSIZE,i+self.BOARDSIZE+1),0] for i in range(4,7)])


        self.boxes.extend([[(i, i+1),(i,i+self.BOARDSIZE),(i+1,i+self.BOARDSIZE+1), (i+self.BOARDSIZE,i+self.BOARDSIZE+1),0] for i in range(8,11)])
        #self.boxes.extend([[(i, i+1),(i,i+self.BOARDSIZE),(i+1,i+self.BOARDSIZE+1), (i+self.BOARDSIZE,i+self.BOARDSIZE+1),0] for i in range(18,23)])
        #self.boxes.extend([[(i, i+1),(i,i+self.BOARDSIZE),(i+1,i+self.BOARDSIZE+1), (i+self.BOARDSIZE,i+self.BOARDSIZE+1),0] for i in range(24,29)])
        #self.boxes.extend([[(i, i+1),(i,i+self.BOARDSIZE),(i+1,i+self.BOARDSIZE+1), (i+self.BOARDSIZE,i+self.BOARDSIZE+1),0] for i in range(30,35)])
        








    def getInitialState(self):
        return TictactoeState(self.board,self._move)
    
    def getPlayer(self,state):
        return self._agents[state._move]
    
    def getActions(self,state):
        possible = []
        for a in range(0, len(self.board)):
            for b in list(range(0, len(self.board))):
                if b == a:
                    continue
                if not self.is_valid(a, b):
                    continue

                if state._board[a].id in state._board[b].partners and state._board[b].id in state._board[a].partners :
                    continue
                possible.append((a, b))
        return possible
    
    def getResult(self, state, action):
        newState = state.copy()
        player = self.getPlayer(state)
        newState._board[self.id_to_index(action[0])].partners.append(action[1])
        newState._board[self.id_to_index(action[1])].partners.append(action[0])
        newState._move = (newState._move + 1) % 2 
        
        winposfound = True
        for pos in self.boxes:
            winposfound = True
            for indpos in pos[:-1]:
        
                if newState._board[self.id_to_index(indpos[0])].id not in newState._board[self.id_to_index(indpos[1])].partners and newState._board[self.id_to_index(indpos[1])].id not in newState._board[self.id_to_index(indpos[0])].partners:
                    winposfound = False
                    break
            if winposfound:
                break 
        
        if winposfound:
            newState._move = -1
            if player._symbol == "X":
                newState._utility = 1
            else:
                newState._utility = -1
        else:
            zeroFound = False
            for a in range(0, len(self.board)):
                for b in list(range(0, len(self.board))):
                    if b == a:
                        continue
                    if not self.is_valid(a, b):
                        continue
                    
                    zeroFound = True
                    break
                
                if zeroFound:
                    break
                
            if not zeroFound:
                newState._move = -1
                newState._utility = 0     
        return newState
    def is_connection(self,id1, id2):
        lit=[]
        for i in self.moves_done:
            lit.append(i.partners)
        if (id1, id2) in lit :
            return True
        if (id2, id1) in lit:
            return True
    def is_valid(self,id1, id2):
        if self.is_connection(id1, id2):
            return False
        p1 = self.board[self.id_to_index(id1)]
        p2 = self.board[self.id_to_index(id2)]
        if (p1.x == p2.x + 100 or p1.x == p2.x - 100) and p1.y == p2.y:
            return True
        if p1.x == p2.x and (p1.y == p2.y + 100 or p1.y == p2.y - 100):
            return True
        return False
    def id_to_index(self,_id):
        for i in range(len(self.board)):
            if self.board[i].id == _id:
                return i
        return -1 
    def terminalTest(self,state):
        return state._move == -1

    def utility(self,state,player): 
        return state._utility
    
    def getAgentCount(self):
        return 2
    
if __name__ == "__main__":
     
    #game = TicTacToeGame()
    """
    #minimax = SimpleMinimax(game)
    initialState = game.getInitialState()
    #minimax.minimax_decision(initialState)
    print(game.getActions())
    #print(initialState)
    print(game.boxes)

    print(game.board)"""


