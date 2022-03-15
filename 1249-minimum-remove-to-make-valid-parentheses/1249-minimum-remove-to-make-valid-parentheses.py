class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=deque()
        
        for pos,i in enumerate(s):
            #print(stack)
            if(i=="("):
                stack.append(["(",pos])
            elif(i==")"):
                if(len(stack)!=0 and stack[-1][0]=="("):
                    stack.pop()
                else:
                    stack.append([")",pos])
        #store positions with extra brackets into a set
        remove=set()
        for i in stack:
            remove.add(i[1])
        ans=""
        #remove them and create ans string
        for pos,i in enumerate(s): 
            if(pos in remove):
                continue
            else:
                ans+=i
        return(ans)