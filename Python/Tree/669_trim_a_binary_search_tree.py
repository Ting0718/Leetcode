class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None

            if root.val < low:
                return dfs(root.right)

            if root.val > high:
                return dfs(root.left)

            else:
                root.left = dfs(root.left)
                root.right = dfs(root.right)

            return root

        return dfs(root)
