# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#BFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        
        while(len(queue)!=0):
            sum,size=0,len(queue)
            for i in range(0,size): # for each level
                ele=queue.popleft()
                #print(ele.val)
                sum+=ele.val
                if ele.left!=None:
                    queue.append(ele.left)
                if ele.right!=None:
                    queue.append(ele.right) 
        return(sum)