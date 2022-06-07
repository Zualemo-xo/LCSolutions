class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans=[]
        p1,p2=0,0
        while(p1<m and p2<n):
            if(nums1[p1]<nums2[p2]):
                ans.append(nums1[p1])
                p1+=1
            else:
                ans.append(nums2[p2])
                p2+=1
        while(p1<m):
            ans.append(nums1[p1])
            p1+=1
        while(p2<n):
            ans.append(nums2[p2])
            p2+=1
            
        for i in range(0,len(ans)):
            nums1[i]=ans[i]
            
        
            