# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #DP Averma TC:O(N) SC:O(h)
        self.ans=float("-inf")
        def helper(node):
            #Base
            if(node==None):
                return(0)
            # Hypothesis
            l=helper(node.left)
            r=helper(node.right)
            
            #Induction
            temp=node.val+max(0,max(l,r)) #For passing value upwards
            res=max(temp,node.val+l+r) # TC: [2,-1]
            self.ans=max(self.ans,res)
            return(temp)
        
        helper(root)
        return(self.ans)
            