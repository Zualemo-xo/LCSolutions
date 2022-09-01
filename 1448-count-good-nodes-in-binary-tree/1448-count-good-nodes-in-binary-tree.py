# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def helper(maxval,node):
            if(node==None):
                return
            else:
                if(maxval<=node.val):
                    self.ans+=1
                helper(max(maxval,node.val),node.left)
                helper(max(maxval,node.val),node.right)
        helper(root.val,root)
        return(self.ans)
        