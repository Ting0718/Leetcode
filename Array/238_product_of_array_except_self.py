# O(n^2) solution
class Solution:
    def product(self, nums1, nums2):
        p = 1
        if not nums1 and not nums2:
            return 0

        for i in nums1:
            p *= i
        for i in nums2:
            p *= i

        return p

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            a = self.product(nums[:i], nums[i+1:])
            res.append(a)

        return res

# O(n) use division


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        product = 1
        for n in nums:
            if n == 0:
                zero += 1
            else:
                product *= n

        res = []
        for n in nums:
            if zero > 1:
                res.append(0)
            else:
                if n == 0:
                    res.append(product)
                else:
                    if zero > 0:
                        res.append(0)
                    else:
                        res.append(int(product / n))

        return res

# Use prefix and postfix array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        if len(nums) <= 1:
            return nums

        p = 1
        for i in range(len(nums)):
            p *= nums[i]
            prefix.append(p)

        p = 1
        for i in range(len(nums)-1, -1, -1):
            p *= nums[i]
            postfix.append(p)

        postfix.reverse()

        res = []
        for i in range(len(nums)):
            if i - 1 < 0:  # first index
                res.append(1 * postfix[i + 1])
            elif i + 1 >= len(nums):
                res.append(prefix[i - 1] * 1)
            else:
                res.append(prefix[i - 1] * postfix[i + 1])

        return res
# save memory
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
