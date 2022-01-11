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
    int sum=0;
    public int helper(TreeNode root,String no){
        if(root==null)
        {
            return(0);
        }
        no+=root.val;
        if(root.left==null && root.right==null)
        {
            sum += Integer.parseInt(no, 2);
            return(0);
        }
        helper(root.left,no);
        helper(root.right,no);
        //System.out.println(sum);
        return(0);      
    }
    public int sumRootToLeaf(TreeNode root) {
        //int no[]=new int[1000];
        String no=new String("");
        helper(root,no);
        return(sum);
    }
}