class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        word=""
        spacecnt=0
        for i in s:
            if(i==" " and word==""):
                continue
            if(i==" "):
                spacecnt+=1
                continue
            
            if(spacecnt>=1):
                spacecnt=0
                stack.append(word+" ")
                word=""
            word+=i

        stack.append(word+" ")
        print(stack)
        ans=[]
        while(len(stack)!=0):
            x=stack.pop()
            if(len(stack)==0): #remove whitespace at end
                
                ans.append(x[:-1])
            else:
                ans.append(x)
        print(ans)
        return(''.join(ans))
            