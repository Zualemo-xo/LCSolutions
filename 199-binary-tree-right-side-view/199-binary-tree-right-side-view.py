# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.levelseen=-1
        self.ans=[]
        def traverse(node,curlevel):
            if (node):
                if(curlevel>self.levelseen):
                    self.levelseen=curlevel
                    self.ans.append(node.val)
                traverse(node.right,curlevel+1)
                traverse(node.left,curlevel+1)
            
        
        traverse(root,0)
        return(self.ans)
        