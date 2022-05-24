class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        
        for i in range(0,len(s)):
            if(s[i]=="("):
                stack.append(i)
            elif(s[i]==")"):
                #print(stack)
                if(len(stack)!=0 and s[stack[-1]]=="("):
                    stack.pop()
                else:
                    stack.append(i)
        maxv=len(s)
        maxn=0
        #print(stack)
        if(len(stack)==0):
            return(len(s))
        while(len(stack)!=0):
            x=stack.pop()
            maxn=max(maxn,maxv-x-1)
            maxv=x
        maxn=max(maxn,maxv)
        return(maxn)