class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        self.ans=[]
        def backtrack(num):
            if(len(num)==n):
                self.ans.append(str(num))
                
            else:
                lastdigit=int(num[-1])
                for i in range(0,10):
                    if(abs(lastdigit-i)==k):
                        num+=str(i)
                        backtrack(num)
                        num=num[:-1]
                
        for i in range(1,10):
            backtrack(str(i))
        return(self.ans)
        