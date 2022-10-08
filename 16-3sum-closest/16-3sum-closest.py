class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sumz=nums[0]+nums[1]+nums[2] 
        # Optimization to 'game' the TLE
        cur = sum(nums[:3])
        if cur >= target:
            return cur
        
        cur = sum(nums[-3:])
        if cur < target:
            return cur
        
        for i in range(0,len(nums)-2):
            left=i+1
            right=len(nums)-1
            while(left<right):   
                if(abs(target-(nums[i]+nums[left]+nums[right]))<abs(target-sumz)):
                    sumz=nums[i]+nums[left]+nums[right]

                if(nums[i]+nums[left]+nums[right]>target):
                    right-=1
                else:
                    left+=1
        return(sumz)
        