# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self,root,k):
        if(root==None):
            return
        if(self.d.get(root.val)!=None):
            self.ans=True
        else:
            self.d[k-root.val]=root.val
        self.helper(root.left,k)
        self.helper(root.right,k)
        
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.ans=False
        self.d={}
        self.helper(root,k)
        return(self.ans)
        
        