# DFS Solution
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Iterative Solution
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        queue = [(root, targetSum - root.val)]
        while queue:
            root, cur_sum = queue.pop(0)
            if not root.left and not root.right and cur_sum == 0:
                return True
            if root.left:
                queue.append((root.left, cur_sum - root.left.val))
            if root.right:
                queue.append((root.right, cur_sum - root.right.val))

        return False
