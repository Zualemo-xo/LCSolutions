class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #TC: O(N) SC:O(N) N-length of ' s  '
        l=[]
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        for i in range(0,len(s)):
            if(s[i] in vowels):
                l.append(s[i])
        
        ans=""
        cnt=len(l)-1
        for i in range(0,len(s)):
            if(s[i] in vowels):
                ans+=l[cnt]
                cnt-=1
            else:
                ans+=s[i]
        return(ans)
            
            
            