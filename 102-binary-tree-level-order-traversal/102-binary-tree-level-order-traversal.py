# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root==None):
            return([])
        q=[]
        ans=[]
        q.append(root)
        while(len(q)):
            li=[]
            for i in range(0,len(q)):
                t=q.pop(0)
                print(t.val)
                li.append(t.val)
                if(t.left!=None):
                    q.append(t.left)
                if(t.right!=None):
                    q.append(t.right)
            ans.append(li)
        return(ans)
            
        