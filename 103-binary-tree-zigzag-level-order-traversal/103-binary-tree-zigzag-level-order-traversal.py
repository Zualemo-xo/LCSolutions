# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
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
                    ans.append(deque([]))
                if(level%2!=0):
                    ans[level].appendleft(node.val)
                else:
                    ans[level].append(node.val)
                #print(ans)
                dfs(node.left,level+1)
                dfs(node.right,level+1)
                #print(ans,level,len(ans))
                
        dfs(root,0)
        return(ans)
            