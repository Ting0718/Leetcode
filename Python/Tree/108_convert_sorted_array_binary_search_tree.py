class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(nums, start, end):
            if end < start:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, start, mid - 1)
            root.right = dfs(nums, mid + 1, end)
            return root

        return dfs(nums, 0, len(nums) - 1)
