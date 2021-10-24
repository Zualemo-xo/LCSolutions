# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def helper(root):
            if(root==None):
                return()
            self.ans+=1
            helper(root.left)
            helper(root.right)
        helper(root)
        return(self.ans)
        