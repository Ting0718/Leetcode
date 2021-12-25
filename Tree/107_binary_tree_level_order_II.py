class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []

        queue = [root]
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                root = queue.pop(0)
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)

            res.append(level)

        return res[::-1]
