class Solution(object):
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True

            if not node.val < right or not node.val > left:
                return False

            # every value on the left less than parent
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
            # every value on the right more than parent

        return valid(root, float("-inf"), float("inf"))
