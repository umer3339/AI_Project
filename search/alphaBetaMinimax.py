#from dotgame.dotBoxesState import DotBoxesState

class AlphaBetaMinimax(object):

    def __init__(self, game, depthlimit=4, listeners = []):

        self._game = game
        self.listeners = listeners
        self._expandedNodes = 0
        self._depthlimit = depthlimit

    
    def minimax_decision(self,state,alpha,beta,depth=0):

        if self._game.terminalTest(state) or depth==self._depthlimit:
            return state._utility
        
        if state.isMax():
            return self.maxvalue(state,alpha,beta,depth)
        else:
            return self.minvalue(state,alpha,beta,depth)
    
    def minvalue(self,state,alpha,beta,depth=0):
	
        self._expandedNodes += 1
        
        retValue = 1000000000000
        retAction = None
        actions = self._game.getActions(state)
        for action in actions:
            if not action==None:
                newState = state.copy()
                tempValue = self.minimax_decision(self._game.getResult(newState,action),alpha,beta,depth+1)
                if tempValue < retValue:
                    retValue = tempValue
                    retAction = action
                if retValue < beta:
                    beta = retValue
                if retValue <= alpha:
                    break

                
        state._action = retAction
        return retValue
            
    def maxvalue(self,state,alpha,beta,depth=0):

        self._expandedNodes += 1
        
        retValue = -1000000000000
        retAction = None
        actions = self._game.getActions(state)
        
        for action in actions:
            if not action==None:
                newState = state.copy()
                takeaction = self._game.getResult(newState,action)
                tempValue = self.minimax_decision(takeaction,alpha,beta,depth+1)
                if tempValue > retValue:
                    retValue = tempValue
                    retAction = action
                
                if retValue > alpha:
                    alpha = retValue

                if retValue >= beta:
                    break

        state._action = retAction
        return retValue
    
