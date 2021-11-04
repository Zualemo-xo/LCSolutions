# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumz=0
        def helper(root):
            #print(root.val)
            print(self.sumz)
            if(root==None):
                return
            elif(root.left==None and root.right!=None):
                helper(root.right)
                return
            elif(root.left==None and root.right==None):
                return
            elif(root.left.left==None and root.left.right==None):
                self.sumz+=root.left.val
                helper(root.right)
                return
            helper(root.left)
            helper(root.right)
        helper(root)
        return(self.sumz)
                