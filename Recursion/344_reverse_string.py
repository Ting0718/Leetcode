class Solution:
    def helper(self, s, l, r):
        if l >= len(s) or r < 0:
            return
        else:
            s[l], s[r] = s[r], s[l]
            self.helper(s, l+1, r-1)

    def reverseString(self, s: List[str]) -> None:
        self.helper(s, 0, len(s)-1)
