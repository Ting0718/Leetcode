class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, l):
            if not root:
                return l
            
            l.append(root.val)
            l = dfs(root.left, l)
            return dfs(root.right, l)
        
        return dfs(root, [])