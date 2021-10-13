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
            if(self.cnt>=len(preorder) or preorder[self.cnt]<leftmin or preorder[self.cnt]>rightmax): #self.cnt>=preorder comes first so that if cnt>len other OR conditions are not checked as they will give error
                #print("cnt:",self.cnt,preorder[self.cnt])
                return(None)
            #if(preorder[cnt]>leftmin and preorder[cnt]<rightmax):
            val=preorder[self.cnt]
            #print(val)
            root=TreeNode(val) #append value to current root
            self.cnt+=1
            root.left=helper(preorder,leftmin,val) #BST SO lower bound is carried from prev iteration,upper bound is the current root val 
            root.right=helper(preorder,val,rightmax) # all values to right are greater than current root val ,with UB starting from infinity
            return(root)
                
        return(helper(preorder,float("-inf"),float("inf")))
            
        
