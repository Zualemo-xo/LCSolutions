from heapq import heapify,heappush,heappop
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while(k>0):
            x=heappop(nums)+1
            heappush(nums,x)
            k-=1
        ans=1
        print(nums)
        for i in nums:
            ans=(ans*i)%1000000007
        return(ans)