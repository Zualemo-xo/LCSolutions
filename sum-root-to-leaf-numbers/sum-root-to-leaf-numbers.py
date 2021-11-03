# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def helper(root,num):
            #print(num,root.val)
            #print(root.val,root.left,root.right)
            if(root==None):
                return
            if(root.left==None and root.right==None):
                num.append(str(root.val))
                print(int(''.join(num)))
                self.ans+=int(''.join(num))
                return
            
            else:
                #print(root,root.val)
                #num.append(str(root.val))
                helper(root.left,num+[str(root.val)])
                helper(root.right,num+[str(root.val)])
        helper(root,[])
        return(self.ans)
        