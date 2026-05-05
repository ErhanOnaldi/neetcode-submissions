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
    public bool IsBalanced(TreeNode root) {
        bool isBalanced = true;

        int Height(TreeNode root)
        {
            if (root is null) return 0;

            int left = Height(root.left);
            int right = Height(root.right);

            if (Math.Abs(left - right) > 1)
                isBalanced = false;

            return 1 + Math.Max(left, right);
        }

        Height(root);
        return isBalanced;
    }
}