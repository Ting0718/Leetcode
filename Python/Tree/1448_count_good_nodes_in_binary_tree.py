# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        queue = [(root, float("-inf"))]
        while queue:
            current, max_val = queue.pop(0)
            if current.val >= max_val:
                count += 1
            if current.left:
                queue.append((current.left, max(max_val, current.val)))
            if current.right:
                queue.append((current.right, max(max_val, current.val)))

        return count