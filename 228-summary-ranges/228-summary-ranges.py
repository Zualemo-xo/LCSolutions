class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans=[]
        if(len(nums)==0):
            return(ans)
        ini,prev=nums[0],nums[0]
        for cur in range(1,len(nums)):
            if(nums[cur]-prev!=1):
                if(ini==prev):
                    ans.append(str(ini))
                else:
                    ans.append(str(ini)+"->"+str(prev))
                ini=nums[cur]
                prev=nums[cur]
                
            elif(nums[cur]-prev==1):
                prev=nums[cur]
                continue
                    
        #for last ele
        if(ini==prev):
            ans.append(str(ini))
        else:
            ans.append(str(ini)+"->"+str(prev))
            
        return(ans)
                
        