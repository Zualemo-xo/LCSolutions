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
    public int helper(TreeNode root,String no){
        if(root==null)
        {
            return(0);
        }
        no+=root.val;
        if(root.left==null && root.right==null)
        {
            return(Integer.parseInt(no, 2));
        }
        //System.out.println(sum);
        return(helper(root.left,no)+helper(root.right,no));      
    }
    public int sumRootToLeaf(TreeNode root) {
        String no=new String("");
        return(helper(root,no));
    }
}