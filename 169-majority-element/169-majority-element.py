class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-Moore Voting Algorithm
        # TC : O(N) SC:O(1)
        tempmajorityele=nums[0]
        count=1
        for i in range(1,len(nums)):
            if(nums[i]!=tempmajorityele):
                count-=1
            else:
                count+=1
            if(count==0):
                tempmajorityele=nums[i]
                count+=1
                
        return(tempmajorityele)