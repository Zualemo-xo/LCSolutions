# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.totsum=0
        def helper(node):
            if(node==None):
                return(0)
            # if(node.left==None):
            #     sumleft=+node.val
            #     return(0)
            # if(node.right==None):
            #     sumright=+node.val
            #     return(0)
            sumleft=helper(node.left)
            sumright=helper(node.right)
            self.totsum+=abs(sumleft-sumright)
            return(sumleft+sumright+node.val)
        helper(root)
        return(self.totsum)