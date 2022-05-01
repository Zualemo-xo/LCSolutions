class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1,s2=deque(),deque()
        for i in s:
            if(i=="#" and len(s1)!=0):
                s1.pop()
            elif(len(s1)==0 and i=="#"):
                continue
            else:
                s1.append(i)
        for i in t:
            if(i=="#"  and len(s2)!=0):
                s2.pop()
            elif(len(s2)==0 and i=="#"):
                continue
            else:
                s2.append(i)
        if(s1==s2):
            return(True)
        return(False)