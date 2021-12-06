class Solution {
    public int minCostToMoveChips(int[] position) {
        int evecount=0,oddcount=0;
        for (int i=0;i<position.length;i++)
        {
            if(position[i]%2==0) //position gives where the marble is located
                evecount+=1;
            else
                oddcount+=1;
        }
        return(Math.min(evecount,oddcount));
    }
}