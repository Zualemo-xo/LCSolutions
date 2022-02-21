class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        maxn,ans=0,0
        for key,val in d.items():
            if(val>maxn):
                maxn=val
                ans=key
        return(ans)
        