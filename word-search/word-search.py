def helper(board,word,row,col,presentword,visited):
    if(row>=len(board) or col>=len(board[0]) or row<0 or col<0):
        return()
    elif([row,col] in visited):
        return()
    elif(board[row][col]!=word[len(presentword)]): #if the next consecutive letter is not in the pattern
        return()
    else:
        visited.append([row,col])
        presentword+=board[row][col]
        #print(presentword)
        if(presentword==word):
            #print(word)
            return(True)
    # return(helper(board,word,row+1,col,presentword,visited) or helper(board,word,row,col+1,presentword,visited) or helper(board,word,row-1,col,presentword,visited) or helper(board,word,row,col-1,presentword,visited))
    # helper(board,word,row+1,col,presentword,visited)
    # helper(board,word,row,col+1,presentword,visited)
    # helper(board,word,row-1,col,presentword,visited)
    # helper(board,word,row,col-1,presentword,visited)
    if(helper(board,word,row+1,col,presentword,visited) or helper(board,word,row,col+1,presentword,visited) or helper(board,word,row-1,col,presentword,visited) or helper(board,word,row,col-1,presentword,visited)):
        return(True)
    visited.pop()
    return(False)
    
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if(word[0]==board[i][j]):
                    if(helper(board,word,i,j,'',[])==True):
                        return(True)
                    #return(helper(board,word,0,0,'',[]))
        return(False)