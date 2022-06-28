class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Sort and perform manipulations
        nums.append(-1)
        nums.append(float("inf"))
        nums.sort()
        cnt=0
        #print(nums)
        for i in range(0,len(nums)-1):
            if(nums[i]==nums[i+1]): #C1: IF EQUAL FREQS
                #nums[i]=nums[i+1]
                nums[i+1]+=1
                cnt+=1
            elif(nums[i]>nums[i+1]): #C2: Occurs due to C1 - increment i+1 based on i
                cnt+=1+nums[i]-nums[i+1]
                nums[i+1]=nums[i]+1
                
            #C3 nums[i]<nums[i+1] NO Changes needed
        #print(nums)
        return(cnt)