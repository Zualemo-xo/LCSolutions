class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum,ans=0,0
        d=defaultdict(int)
        d[0]=1 #initally sum is 0
        for i in range(0,len(nums)):
            sum+=nums[i] #cumilative sum
            if(sum-k in d):
                 ans+=d[sum-k] #increase and by the frequency of sum-k
            d[sum]+=1 #add this cumsum to hashmap,increase frequency by 1
        #print(d)
        return(ans)
        