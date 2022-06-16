class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #TC:O(N^2) SC:0(1)
        self.maxlen=0
        self.ans=""
        def checkpalindrome(left,right):
            while(left>=0 and right<len(s) and s[left]==s[right] ):
                left-=1
                right+=1
            #print(left,right,self.maxlen)
            if(right-left-1>self.maxlen):
                self.maxlen=right-left-1
                self.ans=s[left+1:right] #max len palindrome
            return
                

        for i in range(0,len(s)):
            #print(i,i+1)
            checkpalindrome(i,i) #odd len palindrome word
            checkpalindrome(i,i+1) #even length
        

        return(self.ans)