# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
cnt=0
class Solution:
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #1)obtain inorder list
        inorder=[]
        def helper(root):
            if(root==None):
                return()
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
            
        helper(root)
        #print(inorder)
        #2)Get postfix sum , later assgn to respective values using 'cnt' variable
        postfixsum=[0]*len(inorder)
        for i in range(len(inorder)-1,-1,-1):
            if(i==len(inorder)-1):
                postfixsum[i]=inorder[i]
            else:
                postfixsum[i]=inorder[i]+postfixsum[i+1]
        print(postfixsum)
        def assign(root):
            global cnt
            if(root==None):
                return()
            assign(root.left)
            #print(root.val,postfixsum[cnt],cnt)
            root.val=postfixsum[cnt]
            cnt+=1
            assign(root.right)
            
        assign(root)
        global cnt
        cnt=0
        return(root)