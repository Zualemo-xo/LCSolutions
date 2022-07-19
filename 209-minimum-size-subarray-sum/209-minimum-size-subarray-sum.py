class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        # Sliding window O(n)
        nums=nums+[float("-inf")] #to check last value
        d=deque([])
        ans=float("inf")
        cursum=0
        #front,
        rear=0
        while(rear<len(nums)):
            #print(d,rear)
            if(cursum<k):
                d.append(nums[rear])
                cursum+=nums[rear]
                rear+=1
                #print(rear)
            else:
                curlen=len(d)
                ans=min(curlen,ans)
                ele=d.popleft()
                cursum-=ele
                #front+=1
        return(ans if ans!=float("inf") else 0)
        