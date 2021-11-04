class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.right = left
        root.left = right

        return root

'''bfs solution'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        queue = [root]
        while queue:
            for i in range(len(queue)):
                current = queue.pop(0)
                current.left, current.right = current.right, current.left
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return root

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)

        return root
