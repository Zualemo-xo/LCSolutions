class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Memoization without cache
        #dp=[ [ [-1 for i in range(601)] for j in range (101)] for k in range(101)]
        dp=[[[-1 for col in range(n+1)] for col in range(m+1)] for row in range(len(strs))]
        print(len(dp[0][0]))
        #print(dp)
        def helper(n0,n1,i):
            #processing
            cnt0,cnt1=0,0
            for j in strs[i]:
                if(j=='0'):
                    cnt0+=1
                else:
                    cnt1+=1
            #print(i,cnt0,cnt1,n0,n1)
            #base condn
            if(i<0 or (n0==0 and n1==0)):
                return(0)
            #memoization
            if( dp[i][n0][n1]!=-1):
                return(dp[i][n0][n1])
            #if selected
            if(cnt0<=n0 and cnt1<=n1):
                dp[i][n0][n1]=max( 1 + helper(n0-cnt0,n1-cnt1,i-1),helper(n0,n1,i-1) )
            #if not selected
            elif(cnt0>n0 or cnt1>n1):
                dp[i][n0][n1]=helper(n0,n1,i-1)
            return(dp[i][n0][n1])
                       
        return(helper(m,n,len(strs)-1))