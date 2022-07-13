# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        #TC,SC: O(N)
        #Idea : DFS, Based on qsn condition modify the condition to add into ans array
        ans=[]
        count=[]
        def dfs(node,level):
            
            if(node):
                #print(level,node.val,len(ans))
                if(len(ans)==level): 
                    ans.append(0.0)
                    count.append(0.0)
                    
                #ans[level]=count[level]*ans[level]
                x= count[level]+1
                #print(node.val,count[level]*ans[level])
                ans[level]=((count[level]*ans[level])+ node.val) / x #using maths
                count[level]=x
                
                #print(ans)
                dfs(node.left,level+1)
                dfs(node.right,level+1)
                #print(ans,level,len(ans))
                
        dfs(root,0)
        #print(ans)
        #print(count)
        return(ans)