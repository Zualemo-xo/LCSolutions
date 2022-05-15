# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d=defaultdict(int)
        def helper(root,cnt):
            if(root==None):
                return()
            d[cnt]+=root.val
            helper(root.left,cnt+1)
            helper(root.right,cnt+1)
            
        helper(root,0)
        x=max(d)
        return(d[x])