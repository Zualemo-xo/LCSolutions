class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    
        def bin_search(l,r):
            mid=(l+r)//2
            print(l,r)
            #Base exit conditions
            if(l>=len(arr)):
                return(len(arr)-1)   
            elif(r<0):
                return(0)
            elif(arr[mid]==x or l>r or r<l): #or arr[l]<x<arr[r]
                return(mid)
            
            #Checking conditions
            elif(arr[mid]>x):
                return( bin_search(l,mid-1) )
            else:
                return( bin_search(mid+1,r) )

        pos=bin_search(0,len(arr)-1)
        #print(pos)
        d=deque([])
        l,r=pos,pos+1
        cnt=0
        
        while(cnt<k):
            if( l<0 or ( r<len(arr) and abs(arr[l]-x)>abs(arr[r]-x) ) ):
                d.append(arr[r])
                r+=1
            else:
                d.appendleft(arr[l])
                l-=1
            cnt+=1
            #print(l,r)
        return(d)
        
        
        
            
        