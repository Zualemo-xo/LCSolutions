class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        print(1)
        j=0
        for i in range(0,len(t)):
            if(j==len(s)):
                break
            if(s[j]==t[i]):
                j+=1
        if(j==len(s)):
            return(True)
        else:
            return(False)
