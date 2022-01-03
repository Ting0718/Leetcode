from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        from_left = True
        queue = deque([root])
        res = []
        while queue:
            level = deque()
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    if from_left:
                        level.append(node.val)
                    else:
                        level.appendleft(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            res.append(level)
            from_left = not from_left

        return res
