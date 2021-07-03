class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[0] == "-":
            return False
        else:
            return str(x)[::-1] == str(x)
