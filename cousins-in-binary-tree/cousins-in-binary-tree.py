# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.depth=1
        self.depth1,self.parent1=-1,-1
        self.depth2,self.parent2=-2,-1
        def helper(root,x,y,depth,parent):
            #depth+=1
            if(root==None):
                return()
            if(root.val==x):
                self.depth1=depth
                self.parent1=parent.val
            if(root.val==y):
                self.depth2=depth
                self.parent2=parent.val
            #print(self.depth1,self.depth2)
            helper(root.left,x,y,depth+1,root)
            helper(root.right,x,y,depth+1,root)
        
        helper(root,x,y,0,root)
        print(self.depth1,self.depth2)
        if(self.depth1==self.depth2 and self.parent1!=self.parent2):
            return(True)
        return(False)
            
        