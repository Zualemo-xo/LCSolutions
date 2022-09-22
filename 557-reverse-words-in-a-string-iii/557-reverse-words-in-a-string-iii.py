class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s+=" "
        ans=[]
        temp=[]
        for i in s:
            if(i==" "):
                ans.append(''.join(temp[::-1]))
                temp=[]
            else:
                temp.append(i)
        return(' '.join(ans))
            
        