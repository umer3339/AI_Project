'''
Created on Mar 16, 2019

@author: dr.aarij
'''

import  sys


class SimpleMinimax(object):
    '''
    classdocs
    '''


    def __init__(self, game, listeners = []):
        '''
        Constructor
        '''
        self._game = game
        self.listeners = listeners
        self._expandedNodes = 0
        self._duplicateStates = {}



    def minimax_decision(self,state,depth):
        self._duplicateStates[str(state)] = state
        
        if self._game.terminalTest(state) or  depth ==0 :
            return state._utility
        
        if state.isMax():
            
            return self.maxvalue(state,-1,1,depth)
        else:
            
            return self.minvalue(state,-1,1,depth)
    
    def minvalue(self,state,Alpha,Beta,depth):
        ss = str(state)
        if ss in self._duplicateStates and self._duplicateStates[ss]._utility > state._utility:
            return state._utility
        else:
            self._duplicateStates[str(state)] = state
            
        self._expandedNodes += 1
        
        retValue = 1000000000000
        
#         player = self._game.getPlayer(state)
        actions = self._game.getActions(state)
        
        for action in actions:

            tempValue = self.minimax_decision(self._game.getResult(state,action),depth-1)
           # print("action {}, value {}".format(action,tempValue))

            
            
            if tempValue < retValue:
                retValue = tempValue    
                state._utility = retValue
                state._action = action
                
            if retValue <= Alpha:
                return retValue   
            Beta = min(Beta, retValue)
            if Alpha>=Beta:
                break

        return retValue
            
    def maxvalue(self,state,Alpha,Beta,depth):
        
        ss = str(state)
        if ss in self._duplicateStates and self._duplicateStates[ss]._utility > state._utility:
            return state._utility
        else:
            self._duplicateStates[str(state)] = state
            
        self._expandedNodes += 1
        
        retValue = -1000000000000
        
#         player = self._game.getPlayer(state)
        actions = self._game.getActions(state)
        
        for action in actions:
            tempValue = self.minimax_decision(self._game.getResult(state,action),depth-1)
            #print("action {}, value {}".format(action, tempValue))
            
            if tempValue > retValue:
                retValue = tempValue    
                state._utility = retValue
                state._action = action
                
            if retValue >= Beta:
                return retValue
            #alpha = max(alpha, value)
            Alpha = max(Alpha, retValue)
            if Alpha>=Beta:
                break

        return retValue
