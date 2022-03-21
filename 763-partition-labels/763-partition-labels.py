class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        d=defaultdict(int)
        #find end position
        for i in range(0,len(s)):
            d[s[i]]=i
        #2 pointer
        p1,p2,i=0,d[s[0]],0
        ans=[]
        while(i!=len(s)):
            
            if(d[s[i]]>p2):
                p2=d[s[i]]
            if(i==p2):
                ans.append(p2-p1+1)
                p1=p2+1
            #print(p2)
            
            i+=1
        return(ans)
        