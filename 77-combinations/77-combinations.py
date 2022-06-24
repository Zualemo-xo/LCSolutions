class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #Backtrackig
        ans=[]
        
        def helper(arr,index,sizeleft):
            if(sizeleft==0):
                ans.append(list(arr))
                return
            elif(sizeleft<0):
                return
            else:
                for i in range(index,n+1):
                    arr.append(i)
                    helper(arr,i+1,sizeleft-1)
                    arr.pop()
        helper([],1,k)
        return(ans)
            