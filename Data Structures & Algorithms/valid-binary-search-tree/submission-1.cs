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
    public bool IsValidBST(TreeNode root) {
        bool valid = true;
        List<int> list = new();
        void Dfs(TreeNode root, ref bool validRef)
        {
            if (root is null)
            {
                return;
            }
            Dfs(root.left, ref validRef);
            if (list.Count > 0)
            {
                if (list[^1] >= root.val)
                    validRef = false;
            }
            list.Add(root.val);
            Dfs(root.right,ref validRef);
        }
        Dfs(root, ref valid);
        return valid;

    }
}
