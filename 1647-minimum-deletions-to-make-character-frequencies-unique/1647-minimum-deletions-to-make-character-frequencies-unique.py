class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        cnt=0
        for i in d:
            freq=d[i]
            d[i]=-1
            while( freq in d.values() and freq>0):
                freq-=1
                cnt+=1
            d[i]=freq
        return(cnt)
                