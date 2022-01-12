/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    boolean subtree=false;
    TreeNode ans=null;
    // public TreeNode helper(TreeNode root, int val) {             
    // }
    public TreeNode searchBST(TreeNode root, int val) {
        if(root!=null && subtree==false)
        {
            if(root.val<val)
                searchBST(root.right,val);
            else if(root.val>val)
                searchBST(root.left,val);
            else if(root.val==val)
            {
                ans=root;
                subtree=true;
                //return(root);
            }
        }
        
        return(ans);
        //return(null);
    }
}