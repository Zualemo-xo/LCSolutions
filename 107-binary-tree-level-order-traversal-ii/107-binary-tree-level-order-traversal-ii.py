# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #TC,SC: O(N)
        #Idea : DFS, Based on qsn condition modify the condition to add into ans array
        ans=deque([])

        def dfs(node,level):
            
            if(node):
                #print(level,node.val,len(ans))
                if(len(ans)==level): 
                    ans.appendleft([])
                
                #print(ans)
                dfs(node.left,level+1)
                dfs(node.right,level+1)
                #print(ans,level,len(ans))
                ans[len(ans)-level-1].append(node.val)
        dfs(root,0)
        return(ans)