# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#cnt=0
class Solution(object):
    
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.cnt=0
        root = TreeNode(preorder[0])
        def helper(preorder,leftmin,rightmax):
            #global cnt
            if(self.cnt>=len(preorder) or preorder[self.cnt]<leftmin or preorder[self.cnt]>rightmax):
                #print("cnt:",self.cnt,preorder[self.cnt])
                return(None)
            #if(preorder[cnt]>leftmin and preorder[cnt]<rightmax):
            val=preorder[self.cnt]
            #print(val)
            root=TreeNode(val)
            self.cnt+=1
            root.left=helper(preorder,leftmin,val)
            root.right=helper(preorder,val,rightmax)
            return(root)
                
        return(helper(preorder,float("-inf"),float("inf")))
            
        