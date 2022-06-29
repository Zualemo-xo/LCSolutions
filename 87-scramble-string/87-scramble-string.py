class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # MC W DICT MEMOIZATION & Pruning
        self.memo=defaultdict(bool)
        def solve(a,b):
            # Base conditions

            if(a==b):
                return(True)
            # elif(len(a)==0 or len(b)==0):
            #     return(False)
            #Memo
            key=a+" "+b #Create unique key to be checked/stored in dictionary
            if(key in self.memo): #Return precomputed value
                return(self.memo[key])
            
            #Pruning
            x=sorted(a)
            y=sorted(b)
            #print(x,y)
            if(x!=y): #In case 2 strings have different characters, they can never be equal
                self.memo[key]=False
                return(self.memo[key])
            
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
            self.memo[key]=flag
            return(self.memo[key])
                
        
        
        return(solve(s1,s2))
        