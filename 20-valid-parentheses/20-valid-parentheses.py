class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=deque()
        stack.append(-1)
        symbols={"}":"{","]":"[",")":"("}
        for i in s:
            if(i in symbols.values()):
                stack.append(i)
            if(i in symbols.keys()):
                if(stack[-1]==symbols[i]):
                    stack.pop()
                else:
                    return(False)
        if(len(stack)==1):
            return(True)
        else:
            return(False)