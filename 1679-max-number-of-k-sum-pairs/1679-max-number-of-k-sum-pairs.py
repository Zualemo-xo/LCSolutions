class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        s,e=0,len(nums)-1
        cnt=0
        while(s<e):
            if(nums[s]+nums[e]>k):
                e-=1
            elif(nums[s]+nums[e]<k):
                s+=1
            else:
                cnt+=1
                s+=1
                e-=1
        return(cnt)