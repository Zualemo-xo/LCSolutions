class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt0,cnt=0,0
        for i in range(0,len(word)):
            if(ord(word[0])>64 and ord(word[0])<91 and i==0):
                cnt0+=1
            elif(ord(word[i])>64 and ord(word[i])<91):
                cnt+=1
        if(cnt0==0 and cnt>0):
            return(False)
        elif(cnt0==1 and (cnt+cnt0!=len(word) and cnt+cnt0>1)):
            return(False)
        else:
            return(True)