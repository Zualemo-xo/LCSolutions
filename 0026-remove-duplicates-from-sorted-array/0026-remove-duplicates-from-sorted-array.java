class Solution {
    public int removeDuplicates(int[] nums) {
        int removed=0;
        int n=nums.length;
        for(int i=0;i<n-1;i++)
        {
            if( nums[i] == nums[i+1] )
            {
                nums[i] = 101;
                removed += 1;
            }
            
        }
        
        Arrays.sort(nums);
        return(n-removed);
    }
}