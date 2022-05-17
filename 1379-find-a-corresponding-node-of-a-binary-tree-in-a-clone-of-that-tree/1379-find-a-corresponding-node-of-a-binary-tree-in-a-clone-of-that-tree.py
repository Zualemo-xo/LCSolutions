# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        self.x=TreeNode(1)
        def helper(root):
            
            if(root==None):
                return()
            if(root.val==target.val):
                self.x=root
                return()
            helper(root.left)
            helper(root.right)
        
        helper(cloned)
        return(self.x)
        