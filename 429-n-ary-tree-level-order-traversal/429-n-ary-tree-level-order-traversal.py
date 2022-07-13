"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #TC,SC: O(N)
        #Idea : DFS, Based on qsn condition modify the condition to add into ans array
        ans=deque([])

        def dfs(node,level):
            
            if(node):
                #print(level,node.val,len(ans))
                if(len(ans)==level): 
                    ans.append(deque([]))

                ans[level].append(node.val)
                #print(ans)
                for i in node.children:
                    dfs(i,level+1)
                #print(ans,level,len(ans))
                
        dfs(root,0)
        return(ans)