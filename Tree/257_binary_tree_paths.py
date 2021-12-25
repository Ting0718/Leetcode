# DFS Solution 
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


# BFS Solution
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []

        stack = [(root, str(root.val))]
        res = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))

        return res
