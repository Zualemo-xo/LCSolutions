class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        max_left, max_right = [0 for _ in height], [0 for _ in height]
        for i in range(1, len(height)): # We start at index 1
            # The maximum height at each index is the height of the index 
            # to its immediate left, or the tallest wall at that index    
            max_left[i] = max(height[i-1], max_left[i-1])
        for i in range(len(height)-2, -1, -1): # We start at second    
                                               # rightmost index and go 
                                               # backwards
            max_right[i] = max(height[i+1], max_right[i+1])
        # The below should be almost identical to the brute force solution
        for i in range(1, len(height)-1):
            h = height[i]
            left = max_left[i]
            right = max_right[i]
            if min(left, right) > h:
                res += min(left, right) - h
        return res
        