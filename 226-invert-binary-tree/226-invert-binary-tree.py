# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Keep parent, go 1 level down , and swap left and right pointers in parent, continue till node is not None
        def helper(node):
            if(node==None):
                return
            lchild=node.left
            rchild=node.right
            node.left=rchild
            node.right=lchild
            
            helper(node.right)
            helper(node.left)
            
            
        helper(root)
        return(root)
        