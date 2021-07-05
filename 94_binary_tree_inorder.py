class Solution:
    '''iterative solution'''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        l = []
        while (root or len(stack) != 0):
            while (root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            l.append(root.val)
            root = root.right
        return l


class Solution:
    '''recursive solution'''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.dfs(root, [])

    def dfs(self, root, l):
        if not root:
            return l
        l = self.dfs(root.left, l)
        l.append(root.val)
        return self.dfs(root.right, l)
