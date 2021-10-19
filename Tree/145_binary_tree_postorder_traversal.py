class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, l):
            if not root:
                return l

            l = dfs(root.left, l)
            l = dfs(root.right, l)
            l.append(root.val)

            return l

        return dfs(root, [])