class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #replace 0 by -1 and prefix sum
        for i in range(0,len(nums)):
            if(nums[i]==0):
                nums[i]=-1
            
        ps=[0]*(len(nums)+1)
        ps[0]=nums[0]
        
        for i in range(1,len(nums)):
            ps[i]=nums[i]+ps[i-1]
        #print(ps)
        #hashmap 1st occurence of new sum and length calc by difference
        d=defaultdict(int)
        d[0]=-1 #count before starting traversal of array
        maxn=0
        for i in range(0,len(nums)):
            if(ps[i] not in d):
                d[ps[i]]=i
            else:
                maxn=max((i-d[ps[i]]),maxn)
                #print(maxn,d)
        return(maxn)