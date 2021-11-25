class Solution {
    public int maxSubArray(int[] nums) {
        int s=0,max=0;
        double maxno=Double.NEGATIVE_INFINITY;
        for(int i=0;i<nums.length;i++)
        {
            if(maxno<nums[i])
            {
                maxno=nums[i];
            }
            s+=nums[i];
            if(s<0)
                s=0;
            else if(s>max)
                max=s;
        }  
        if(s==0 && maxno<0)
            return((int)maxno);
        else
            return(max);
      
    }
}