class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        cnt,ans=0,[]
        #print(d)
        for i in sorted(d.items(), key=lambda kv: kv[1],reverse=True):
            #print(i)
            if(cnt==k):
                break
            ans.append(i[0])
            cnt+=1
        return(ans)