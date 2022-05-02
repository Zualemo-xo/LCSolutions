class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        g,s=len(nums)-1,0
        
        while(g>s):
            if(nums[s]%2==0):
                s+=1
            elif(nums[g]%2!=0):
                g-=1
            else:
                nums[g],nums[s]=nums[s],nums[g]
                g-=1
                s+=1
        return(nums)