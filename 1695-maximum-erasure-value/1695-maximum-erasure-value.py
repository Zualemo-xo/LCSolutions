class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #SWINDOW
        s=set()
        ans=0
        cursum=0
        p1,p2=0,0
        while(p2!=len(nums)):
            ans=max(cursum,ans)
            #print(p1,p2,cursum,s)
            if(p1==p2):
                s.add(nums[p2])
                cursum=nums[p1]
                p2+=1
                #ans=max(cursum,ans)
            elif(nums[p2] in s):
                while(True):
                    
                    if(nums[p1]==nums[p2]):
                        #cursum-=nums[p1] # AS WE NEED TO ADD nums[p2 anyway this gets neutralized]
                        #s.add(nums[p2])
                        p1+=1
                        p2+=1
                        break
                    else:
                        s.remove(nums[p1])
                        cursum-=nums[p1]
                        p1+=1
            elif(nums[p2] not in s):
                s.add(nums[p2])
                cursum+=nums[p2]
                p2+=1
        ans=max(cursum,ans)
        return(ans)