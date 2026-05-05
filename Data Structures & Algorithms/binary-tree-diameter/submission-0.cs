/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public int DiameterOfBinaryTree(TreeNode root) {
        int max = 0;
        int Height(TreeNode root, ref int maxRef)
        {
            if (root is null) return 0;
            int leftDepth = Height(root.left, ref maxRef);
            int rightDepth = Height(root.right, ref maxRef);
            maxRef = Math.Max(maxRef, leftDepth + rightDepth);
            return 1 + Math.Max(leftDepth, rightDepth);
        }
        Height(root, ref max);
        return max;
    }
}