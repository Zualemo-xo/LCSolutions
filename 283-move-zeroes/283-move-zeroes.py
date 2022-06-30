class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zerocnt=0
        for i in nums:
            zerocnt=zerocnt+1 if i == 0 else zerocnt
        n=len(nums)
        for i in range(zerocnt):
            nums.append(0)
        print(nums)
        #for i in range(0,n):
        i=0
        cnt=0
        while(cnt<n):
            #print(i,nums)
            if(nums[i]==0):
                x=nums.pop(i)
            else:
                i+=1
            cnt+=1
        return(nums)
            
                
            