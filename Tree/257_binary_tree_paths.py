class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, s):
            if root:
                s += str(root.val)

                if not root.left and not root.right:
                    paths.append(s)
                else:
                    s += "->"
                    dfs(root.left, s)
                    dfs(root.right, s)

        paths = []
        dfs(root, "")
        return paths
