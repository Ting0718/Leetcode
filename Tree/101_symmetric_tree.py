# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''DFS Solution'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymm(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return isSymm(l.left, r.right) and isSymm(l.right, r.left)
            return False
        return isSymm(root, root)

'''BFS Solution'''
class Solution(object):
    def isSymmetric(self, root):
        queue = [(root, root)]
        while queue:
            l, r = queue.pop(0)
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            else:
                queue.append((l.left, r.right))
                queue.append((l.right, r.left))

        return True
