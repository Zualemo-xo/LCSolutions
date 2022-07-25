class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary search 
        front,back=0,len(nums)-1
        start,end=-1,-1
        while(front<=back):
            
            mid=(front+back)//2
            if(nums[mid]==target):
                start=mid
                end=mid
                while(start!=0 and nums[start]==nums[start-1]):
                    start-=1
                while(end!=len(nums)-1 and nums[end]==nums[end+1]):
                    end+=1
                break
                    
            elif(nums[mid]<target):
                front=mid+1
            elif(nums[mid]>target):
                back=mid-1
        
        return([start,end])