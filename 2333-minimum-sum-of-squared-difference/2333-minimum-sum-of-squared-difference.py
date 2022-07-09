
class Solution:
    def minSumSquareDiff(self, n1: List[int], n2: List[int], k1: int, k2: int) -> int:
        #Bucket Sort of diff TC,SC:O(n)
        freq=[0]*(10**5+1)
        k=k1+k2
        for i in range(0,len(n1)):
            freq[ abs(n1[i]-n2[i]) ]+=1
        #print(freq[-3:]) 
        for i in range(len(freq)-1,0,-1):
            if(freq[i]>0):
                subtracted=min(k,freq[i])
                freq[i-1]+=subtracted
                freq[i]-=subtracted
                k-=subtracted
        #For 0 case , we dont want to store anything in 10**5 array
        if(freq[i]>0):
                subtracted=min(k,freq[i])
                freq[i]-=subtracted
                k-=subtracted
        ans=0 
        #print()
        #print(freq[-3:])
        for i in range(0,len(freq)): 
            ans+=freq[i]*(i)**2
        return(ans)
                    