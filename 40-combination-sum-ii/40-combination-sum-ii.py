class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(arr,cursum,index):
            #print(arr,index)
            if(target==sum(arr)):
                #print(cursum,arr)
                #arr.sort()
                #if(arr not in self.ans):
                self.ans.append(list(arr))
                return
            if(target<cursum):
                return
            for i in range(index,len(candidates)):
                if(i>index and candidates[i]==candidates[i-1]):
                    continue
                arr.append(candidates[i])
                helper(arr,cursum+candidates[i],i+1)
                arr.pop()

        self.ans=[]
        candidates.sort()
        helper([],0,0)
        return(self.ans)
        