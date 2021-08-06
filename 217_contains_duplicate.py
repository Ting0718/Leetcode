'''hashmap solution'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        visited = {}
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited[nums[i]] = 0
            visited[nums[i]] += 1
            if visited[nums[i]] > 1:
                return True

        return False

'''compare previous solution'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False

'''compare set length with array length solution'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
