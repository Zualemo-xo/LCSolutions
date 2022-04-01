class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        fin=len(s)-1
        for i in range(0,len(s)//2):
            s[i],s[fin]=s[fin],s[i]
            fin-=1
            