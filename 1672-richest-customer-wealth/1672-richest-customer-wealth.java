class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxs=0;
        for(int i=0;i<accounts.length;i++)
        {
            int cursum=0; 
           for(int j=0;j<accounts[i].length;j++)
           {
               cursum+=accounts[i][j];
           }
            if(cursum>maxs)
               maxs=cursum; 
        }
        return(maxs);
    }
}