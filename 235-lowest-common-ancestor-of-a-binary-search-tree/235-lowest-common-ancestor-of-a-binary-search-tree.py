# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            # TC: O(H) SC:O(H)
            while(node!=None):
                if(node.val>p.val and node.val>q.val):
                    return( helper(node.left) )
                elif( node.val<p.val and node.val<q.val ):
                    return( helper(node.right) )
                else: # when p<node.val <q or vice versa
                    return(node)
        return(helper(root))