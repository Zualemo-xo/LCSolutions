# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
            
        def helper(node):
            q=deque([(node,-1)])
            foundx=False
            parentx=-1
            foundy=False
            parenty=-1
            
            while(len(q)!=0):
                cnt=len(q)
                
                while(cnt!=0):
                    cnt-=1
                    ele,parent=q.popleft()
                    
                    if(ele==None):
                        continue
                    #print(ele.val,parent.val)
                    if(ele.val==x):
                        foundx=True
                        parentx=parent
                    if(ele.val==y):
                        foundy=True   
                        parenty=parent
                    q.append((ele.left,ele))
                    q.append((ele.right,ele))
                    
                if(foundx==True and foundy==True and (parentx!=parenty)):
                    return(True)
                elif(foundx==True or foundy==True):
                    return(False)
            return(False)
        
        answer=helper(root)
        return(answer)
                
        
        
        