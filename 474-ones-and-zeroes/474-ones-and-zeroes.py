class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
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
            
            #if selected
            if(cnt0<=n0 and cnt1<=n1):
                return(max( 1 + helper(n0-cnt0,n1-cnt1,i-1),helper(n0,n1,i-1) ))
            #if not selected
            elif(cnt0>n0 or cnt1>n1):
                return(helper(n0,n1,i-1))       
                       
        return(helper(m,n,len(strs)-1))