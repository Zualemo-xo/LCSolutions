# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def helper(node):
            # Base
            if(node==None):
                return(0)
            #Hypo
            l=helper(node.left)
            r=helper(node.right)

            #Induc
            #Edge cases to deal with leaf nodes or nodes without left or right values
            if(node.left==None and node.right==None):
                l=0 
                r=0
                temp=1
                self.ans=max(self.ans,temp)
            elif(node.left==None):
                l=0
                if(node.right.val==node.val): #If left child ''
                    temp=r+1
                    self.ans=max(self.ans,temp)
                else: #choose l=0 as starting leaf node for search
                    temp=1
                    self.ans=max(self.ans,temp)
            elif(node.right==None):
                r=0
                if(node.left.val==node.val): #If right child has different value
                    temp=l+1
                    self.ans=max(self.ans,temp)
                else: #choose r=0 as starting leaf node for search
                    temp=1
                    self.ans=max(self.ans,temp)


            else: #Assign temp value based oon whether child nodes are equal to current node.
                if(node.left.val==node.val and node.right.val==node.val): # Both children nodes have same value as current parent node
                    temp=max(l,r)+1
                    self.ans=max(self.ans,l+r+1)
                elif(node.left.val==node.val): #If right child has different value
                    temp=l+1
                    self.ans=max(self.ans,temp)
                elif(node.right.val==node.val): #If left child ''
                    temp=r+1
                    self.ans=max(self.ans,temp)
                else: #Both l and r child nodes are not equal to curr node
                    temp=1
                    self.ans=max(self.ans,temp)

            return(temp)
        
        helper(root)
        return(max(0,self.ans-1))