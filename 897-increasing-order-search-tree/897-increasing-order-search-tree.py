# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        rtree=self.ans=TreeNode(-1)
        #inorder traversal, add into rtree new right nodes
        def helper(root):
            if(root==None):
                return()
            helper(root.left)
            self.ans.right=TreeNode(root.val)
            self.ans=self.ans.right
            helper(root.right)        
        helper(root)
        return(rtree.right)