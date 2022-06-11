class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Sliding Window to find subarray
        sumarr=sum(nums)
        n=len(nums)

        tofind=sumarr-x # a subarray of this value with max length
        if(tofind<0): # EDGE: [1,1] 3
            return(-1)
        if(tofind==0): #EDGE: TARGET AND SUM OF ARR ARE EQUAL[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309] 134365
            return(len(nums))
        l,r=0,0
        cursum=nums[0]
        cnt,ans=0,0
        while(r<len(nums)):
            if(cursum==tofind):
                print(tofind,l,r)
                ans=max(ans,r-l+1)
                r+=1
                if(r<len(nums)):
                    cursum+=nums[r]
            elif(cursum<tofind):
                r+=1
                if(r<len(nums)):
                    cursum+=nums[r]
            elif(cursum>tofind):
                l+=1
                cursum-=nums[l-1]
        
        if(ans==0):
            return(-1)
        else:
            return(n-ans)