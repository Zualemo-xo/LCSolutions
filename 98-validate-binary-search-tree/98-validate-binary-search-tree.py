# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isholds=True
        def recursion(node,minval,maxval):
            if(node==None):
                return
            
            recursion(node.left,minval,node.val)
            if(minval>=node.val or node.val>=maxval):
                #print(node.val)
                self.isholds=False
            recursion(node.right,node.val,maxval)

        
        recursion(root,float("-inf"),float("inf"))
        return(self.isholds)