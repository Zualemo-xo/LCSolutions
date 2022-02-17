class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        
        def helper(arr,index,sumz):
            if(sumz==target):
                ans.append(list(arr)) #list() allows to hold not the pointer but the eles in the list ig
                #print(sumz,arr)
            if(sumz>=target):
                return()
            
            
            for i in range(index,len(candidates)):
                arr.append(candidates[i])
                helper(arr,i,sumz+candidates[i])
                arr.pop() #backtracking
                
        ans=[]
        helper([],0,0)
        return(ans)
        
        

        