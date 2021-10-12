'''recursive solution'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


'''iterative solution (Breath first search)'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return depth
        
        queue = []
        while queue:
            depth += 1
            for i in range(len(queue)):
                current_node = queue.pop(0)
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)
        
        return depth