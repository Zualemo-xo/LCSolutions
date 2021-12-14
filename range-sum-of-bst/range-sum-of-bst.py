# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum=0
        def helper(root):
            if(root==None):
                return
            if(root.val>=low and root.val<=high):
                self.sum+=root.val
            helper(root.left)
            helper(root.right)
        helper(root)
        return(self.sum)
        