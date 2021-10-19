'''use python in-built function'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


'''iteratively swap left and right'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1

'''recursively swap left and right'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                helper(l + 1, r - 1)

        helper(0, len(s)-1)
