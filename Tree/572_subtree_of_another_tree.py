class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root:
            return False

        def isSameTree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False

            return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
