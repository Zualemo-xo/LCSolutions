class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        prod0=1
        ans=[]
        for i in nums:
            if(i!=0):
                prod0*=i
            prod*=i
        for i in nums:
            if(i==0):
                first0=nums.index(0)
                last0=len(nums) - nums[::-1].index(0) - 1
                #print(first0,last0)
                if(first0==last0): #product not 0 as there is only 1 0
                    ans.append(prod0)
                else:
                    ans.append(prod)
            else:
                ans.append(prod//i)
        return(ans)
        