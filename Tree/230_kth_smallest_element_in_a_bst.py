'''Recursion'''
class Solution(object):
    def kthSmallest(self, root, k):
        def dfs(root, l):
            if not root:
                return l
            l = dfs(root.left, l)
            l.append(root.val)
            return dfs(root.right, l)

        res = dfs(root, [])
        return res[k-1]

'''Iterative Solution'''
class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        l = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            l.append(root.val)
            root = root.right

        return l[k-1]
