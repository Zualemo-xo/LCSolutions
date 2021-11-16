class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        print(nums)
        ans=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if(nums[i]%nums[j]==0):
                    ans[i]=max(ans[i],ans[j]+1)
                    
        print(ans)
        maxans=max(ans)
        print(maxans)
        curpos=len(nums)-1
        print(curpos)
        l=[]
        prev=-1
        while(curpos>=0 and maxans>0):
            #print(l[len(l)-1],ans[curpos])
            if(maxans==ans[curpos] and (prev==-1 or prev%nums[curpos]==0)):
                l.append(nums[curpos])
                maxans-=1
                prev=nums[curpos]
            curpos-=1
        return(l)
        
        