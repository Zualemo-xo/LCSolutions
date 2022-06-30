class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # MCM+Memoization with binary search
        #TC:O(log(N)*N*K), SC:O(N*K)
        #memo=defaultdict(int)
        @cache
        def solve(e,f):
            # Base
            #key=str(e)+" "+str(f)
            #if(key in memo):
                #return(memo[key])
            if(f==0 or f==1):
                return(f)
            elif(e==0 or e==1):
                return(f)
            
            #MCM
            #print(e,f)
            
            #Binary Search
            l=1
            r=f
            minv=float("inf")
            
            while(l<=r):
                mid=(l+r)//2 #Find mid at every iter
                
                left=solve(e,f-mid) 
                right=solve(e-1,mid-1)
                if(left>right): #We have to traverse towards up of building
                    l=mid+1
                else: #Go down , as the threshold poit is there
                    r=mid-1
            
                #           Egg breaks  Egg does not break
                temp=1+max(left,right)
                minv=min(temp,minv)
                #memo[key]=minv
            return(minv)
        
        return(solve(k,n))