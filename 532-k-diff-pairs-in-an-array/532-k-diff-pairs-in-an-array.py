class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #two pointers
        l,r,ans=0,1,0
    
        if(k==0): #edge case
            d=defaultdict(int)
            for i in nums:
                d[i]+=1
            for i in d:
                if(d[i]>1):
                    ans+=1
            return(ans)
        
        nums=list(set(nums)) #remove duplicates
        nums.sort()
        while(r<len(nums)):
            #print(l,r,nums[l],nums[r])
            if(abs(nums[r]-nums[l])==k):
                ans+=1
                r+=1
                l+=1
            elif(abs(nums[r]-nums[l])>k):
                l+=1
            elif(abs(nums[r]-nums[l])<k):
                r+=1
            if(l==r):
                r+=1
        return(ans)