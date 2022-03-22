class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans=[]
        k-=n #subtract the present 'a' added in as placeholder
        for i in range(n):
            ans.append(1)
        for i in range(n-1,-1,-1):
            if(k<=25):
                ans[i]=k+1
                break
            ans[i]=26 
            k=k-25 
            #print(k)  
        #print(ans)
        for i in range(len(ans)):
            ans[i]=chr(96+ans[i])
        return("".join(ans))
            