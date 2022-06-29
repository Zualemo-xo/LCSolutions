class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # MC W CACHE MEMOIZATION
        @cache
        def solve(a,b):
            # Base conditions

            if(a==b):
                print("vf")
                return(True)
            elif(len(a)==0 or len(b)==0):
                return(False)

            # MCM
            flag=False
            n=len(a)
            for i in range(1,n):
                #CASE A

                if(solve(a[:i],b[-i:])==True and solve(a[i:],b[:-i])==True):
                    flag=True
                    break
                #CASE B
                if(solve(a[:i],b[:i])==True and solve(a[i:],b[i:])==True):
                    flag=True
                    break
            return(flag)
                
        
        
        return(solve(s1,s2))
        