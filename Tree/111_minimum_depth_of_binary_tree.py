class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                current = queue.pop(0)
                if not current.left and not current.right:
                    return depth
                if current.left:
                    queue.append(current.left)
                if not current.right:
                    queue.append(current.right)

        return depth
