# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.v=0
        def helper(root,maxn,minn):
            if(root==None):
                return()
            if(maxn<root.val):
                maxn=root.val
            if(minn>root.val):
                minn=root.val
            if(maxn!=float("-inf") and minn!=float("inf") and abs(maxn-minn)>self.v):
                self.v=abs(maxn-minn)
            helper(root.left,maxn,minn)
            helper(root.right,maxn,minn)
        helper(root,float("-inf"),float("inf"))
        return(self.v)
        