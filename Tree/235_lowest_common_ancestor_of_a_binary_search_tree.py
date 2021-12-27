# DFS Solution
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        parent_val = root.val

        p_val = p.val
        q_val = q.val

        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


# Iterative Approach
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            parent_val = node.val
            if p_val < parent_val and q_val < parent_val:
                node = node.left
            elif p_val > parent_val and q_val > parent_val:
                node = node.right
            else:
                return node
