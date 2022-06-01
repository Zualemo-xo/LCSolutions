"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        #DFS
        if(node==None): #for edge case [] 
            return(None)
        #create stack,dict to hold OG link with new link
        d=defaultdict(Node)
        stack=[node]
        visited=defaultdict(int)
        visited[node]+=1 # Initialization
        
        while(len(stack)!=0):
            curr=stack.pop()
            #print(curr.val)

            if(curr not in d):
                newclone=Node(curr.val)
                d[curr]=newclone
            else:
                newclone=d[curr] #retrive already created clone node location
            
            for old_n in curr.neighbors:
                if(old_n in d): #clone ref for that point already created
                    newclone.neighbors.append(d[old_n])
                else: #create new ref 
                    futureclone=Node(old_n.val)
                    d[old_n]=futureclone
                    newclone.neighbors.append(d[old_n])
            #Add new ele to stack
            for old_n in curr.neighbors:
                if(old_n not in visited):
                    stack.append(old_n)
                    visited[old_n]+=1
        
        #print(d[node].neighbors)
        return(d[node])
                