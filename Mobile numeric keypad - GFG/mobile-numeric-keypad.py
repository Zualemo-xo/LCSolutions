#User function Template for python3
class Solution:
	def getCount(self, N):
		# code here
		phonepad=[[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
        # memo[n][1-9]
        memo=[[-1 for i in range(10)] for i in range(N)]
        
        def isValid(x,y):
            if(x>=0 and y>=0 and x<len(phonepad) and y<len(phonepad[0]) and phonepad[x][y]!=-1):
                return(True)
            return(False)
            
        def solve(r,c,noleft):
            x=[0,0,1,-1,0]
            y=[-1,1,0,0,0]
            if(memo[noleft][phonepad[r][c]]!=-1):
                return(memo[noleft][phonepad[r][c]])
            if(noleft==0):
                return(1)
            cnt=0
            for i in range(0,5):
                if(isValid(r+x[i],c+y[i])):
                    cnt=cnt+solve(r+x[i],c+y[i],noleft-1)
            memo[noleft][phonepad[r][c]]=cnt
            return(cnt)
            
            
        ans=0
        for i in range(len(phonepad)):
            for j in range(len(phonepad[0])):
                if(phonepad[i][j]!=-1):
                    ans+=solve(i,j,N-1)
        return(ans)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.getCount(N)
		print(ans)

# } Driver Code Ends