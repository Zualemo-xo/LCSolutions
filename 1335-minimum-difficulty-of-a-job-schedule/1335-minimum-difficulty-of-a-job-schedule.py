class Solution:
    def minDifficulty(self, job: List[int], day: int) -> int:
        if(len(job)<day): #edge case
            return(-1)
        maxdif=[job[-1]]*len(job)
        for i in range(len(job)-2,-1,-1):
            maxdif[i]=max(maxdif[i+1],job[i])
        #print(maxdif)
        @lru_cache(None)
        def helper(jobsdone,curday):
            if(curday==day):
                return(maxdif[jobsdone])
            
            best = float("inf")
            tbd=len(job)-(day-curday)
            hardon=0
            #print(tbd)
            for i in range(jobsdone,tbd):
                hardon=max(hardon,job[i])
                best=min(best,hardon+helper(i+1,curday+1))
            return(best)
            
        return(helper(0,1))
            
        
        