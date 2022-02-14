# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self,root,cnt):
        if(root==None):
            return
        else:
            cnt+=1
            self.helper(root.left,cnt)
            self.helper(root.right,cnt)
            if(cnt>self.maxn):
                self.maxn=cnt
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxn=0
        self.helper(root,0)
        return(self.maxn)
        