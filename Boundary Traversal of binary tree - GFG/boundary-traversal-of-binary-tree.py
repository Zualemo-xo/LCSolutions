#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        ans=[]
        def leaves(node):
            if(node!=None):
                if(node.left==None and node.right==None):
                    ans.append(node.data)
                leaves(node.left)
                leaves(node.right)
            
        def left(node):
            if(node!=None):
                if(node.left!=None):  #Ignore alreadty added leaf nodes
                    ans.append(node.data)
                    left(node.left)
                elif( node.right!=None):
                    ans.append(node.data)
                    left(node.right)
        def right(node):
            if(node!=None):
                if( node.right!=None):
                    right(node.right)
                    ans.append(node.data)
                elif(node.left!=None):  #Ignore alreadty added leaf nodes
                    right(node.left)
                    ans.append(node.data)
                    
                
                    
            
        ans.append(root.data)
        left(root.left)
        
        leaves(root.left)
        leaves(root.right)
        right(root.right)
        #print(ans)
        return(ans)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{ 
#  Driver Code Starts
import sys

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')
# } Driver Code Ends