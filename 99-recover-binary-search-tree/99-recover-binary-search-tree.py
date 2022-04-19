# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.l=[]
        def helper(root):
            if(root==None):
                return
            helper(root.left)
            self.l.append(root.val)
            helper(root.right)
        helper(root)
        self.l.sort()
        self.cnt=0
        def helper1(root):
            if(root==None):
                return
            helper1(root.left)
            root.val=self.l[self.cnt]
            self.cnt+=1
            helper1(root.right)
        helper1(root)