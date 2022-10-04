# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ans=0
t=False
def countz(self, root, targetSum,cnt):
    global ans
    if (root==None):
        return(False)
    elif(root.left==None and root.right==None):
        print(cnt)
        if(cnt+root.val==targetSum):
            print("d")
            ans+=1
            return(True)
        return(False)     

    cnt+=root.val

    t1=countz(self, root.left, targetSum,cnt)
    if(t1):
        return(True)
    t2=countz(self, root.right, targetSum,cnt)
    if(t2):
        return(True)
    return(False)
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        cnt=0
        if not (root):
            return(False)
        return(countz( self,root, targetSum,cnt))

