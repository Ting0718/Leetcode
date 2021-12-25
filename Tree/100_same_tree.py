class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution(object):
    def isSameTree(self, p, q):
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        queue = [(p, q)]
        while queue:
            p, q = queue.pop(0)
            if not check(p, q):
                return False

            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
