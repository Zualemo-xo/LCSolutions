/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
// TC: O(log N) SC:O(1)
public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int min=0,max=n,mid,api;
        while(true)
        {
            mid=min+(max-min)/2;
            api=guess(mid);
            if(api==0)
            {
                return(mid);
            }
            
            else if(api==1)
            {
                min=mid+1;
            }
            else{
                max=mid-1;
            }
        }
        
    }
}