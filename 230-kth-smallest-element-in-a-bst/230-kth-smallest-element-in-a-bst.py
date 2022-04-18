# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt=0
        self.ans=-1
        def helper(root):
            if(root):
                helper(root.left)
                self.cnt+=1
                if(self.cnt==k):
                    self.ans=root.val
                helper(root.right)
            else:
                return()
        helper(root)
        return(self.ans)