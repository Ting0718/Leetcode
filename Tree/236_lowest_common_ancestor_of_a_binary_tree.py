class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # if the current node = p or q
        if root.val == p.val or root.val == q.val:
            return root
        # leaf node
        if not root.left and not root.right:
            return None

        left, right = None, None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # both left child and right child are nodes
        if left and right:
            return root

        if not left:
            return right
        else:
            return left
