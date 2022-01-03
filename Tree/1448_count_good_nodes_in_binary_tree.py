
'''BFS'''
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

'''DFS'''
class Solution(object):
    def goodNodes(self, root):
        self.count = 0

        def dfs(root, max_num):
            if not root:
                return
            if root.val >= max_num:
                self.count += 1
            if root.left:
                dfs(root.left, max(max_num, root.val))
            if root.right:
                dfs(root.right, max(max_num, root.val))

        dfs(root, float("-inf"))
        return self.count
