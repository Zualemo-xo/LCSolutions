# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #self.val=1 -----> has camera
        # self.val=0 -----> needs camera
        #self.val=2     curr node covered by child
        #self.val==-1 NOT NEEDED (None Case)
        self.ans=0
        def helper(node):
            #base
            if(node==None): #None node never needs a camera
                return(-1)
            #hypothesis
            l=helper(node.left)
            r=helper(node.right)

            #induction
            #edge cases
            if(node.left==None and node.right==None): #Leaf node is never a camera (as unoptimal) , but needs camera
                temp=0
            elif(node.left==None): #Curr node can be a camera if right child is not a camera
                if(r==1):
                    temp=2
                elif(r==0):
                    temp=1
                    self.ans+=1
                elif(r==2): 
                    temp=0 #needs camera but child is covered , hence curr node will not be camera
            elif(node.right==None):
                if(l==1):
                    temp=2
                elif(l==0):
                    temp=1
                    self.ans+=1
                elif(l==2):
                    temp=0
            #normal cases
            else:
                if(l==1 and r==1): #curr node is also covered
                    temp=2 #since both child nodes are covered
                elif(l==0 or r==0): #either child is not covered, current node has to become camera
                    temp=1
                    self.ans+=1
                elif((l==1 and r==2) or (l==2 and r==1)):
                    temp=2
                else:
                    temp=0 #when child node is covered but curr nodes needs camera from parent in future
            return(temp)
        
        x=helper(root)
        print(x)
        return(self.ans if x!=0 else self.ans+1) # to handle TC:[0] , [0,null,0,null,0,null,0] :WHEN ROOT NODE NEEDS TO BE A CAMERA