class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nge=[-1]*(len(nums2))

        for i in range(0,len(nums2)):
            for j in range(i+1,len(nums2)):
                if(nums2[j]>nums2[i]):
                    nge[i]=nums2[j]
                    break
        ans=[]
        for i in nums1:
            ans.append(nge[nums2.index(i)])
        return(ans)
