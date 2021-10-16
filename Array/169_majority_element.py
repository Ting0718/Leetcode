
'''hashMap Solution'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        times = len(nums)/2
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

            if hash_map[i] > times:
                return i

'''sort Solution'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

''' Boyer-Moore Voting Algorithm'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
