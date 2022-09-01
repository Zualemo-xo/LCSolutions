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
        def helper(maxval,node):
            if(node==None):
                return(0)
            else:
                if(maxval<=node.val):
                    return(1+helper(node.val,node.left)+helper(node.val,node.right))
                else:
                    return(helper(maxval,node.left)+helper(maxval,node.right))
                
        return( helper(root.val,root) )

        