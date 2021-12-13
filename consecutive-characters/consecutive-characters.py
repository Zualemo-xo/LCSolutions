class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxl,localcnt=1,0
        isfirst=True
        for i in range(1,len(s)):
            if(s[i-1]==s[i]):
                localcnt+=1
                if(isfirst==True):
                    isfirst=False
                    localcnt+=1
                    
            if((s[i-1]!=s[i] and localcnt!=0) or (i==len(s)-1)):
                if(maxl<localcnt):
                    maxl=localcnt
                localcnt=0
                isfirst=True
        return(maxl)