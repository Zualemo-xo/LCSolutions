#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		ans=0
		while(n!=0):
		    #print(n & 1)
		    bit=n & 1
		    ans=ans+1 if bit else ans
		    n=n>>1
		return(ans)   

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends