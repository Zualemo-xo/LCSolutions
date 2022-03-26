class Solution(object):
    def helper(self,nums,front,back,target):
        mid=front+(back-front)//2
        print(nums[mid],front,back)
        if(front>back):
            return(-1)
        elif(nums[mid]==target):
            return(mid)
        elif(target>nums[mid]):
            return(self.helper(nums,mid+1,back,target))
        elif(target<nums[mid]):
            return(self.helper(nums,front,mid-1,target))
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        front,back=0,len(nums)-1
        return(self.helper(nums,front,back,target))     