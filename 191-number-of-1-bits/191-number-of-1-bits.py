class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while(n!=0):
            bit=n & 1 #Find out if the end digit is 1 or 0 using AND
            if(bit==1):
                ans+=1
            n=n>>1 #REMOVE last digit to proceed with next iteration
        return(ans)