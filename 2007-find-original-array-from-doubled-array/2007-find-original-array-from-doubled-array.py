class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        d=defaultdict(int)
        for i in changed:
            d[i]+=1
        cnt=0
        ans=[]
        changed.sort()
        for i in changed:
            if(2*i in d and d[i]!=0 and d[2*i]!=0):
                d[i]-=1
                d[2*i]-=1
                if(d[2*i]>=0):
                    ans.append(i)
                    cnt+=1
        print(cnt,ans)
        if(len(changed)%2==0 and cnt==len(changed)//2):
            return(ans)
        else:
            return([])
        