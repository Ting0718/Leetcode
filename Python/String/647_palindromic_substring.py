'''brute force'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s1, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True
        
        res = 0
        for l in range(len(s)):
            for r in range(l, len(s)):
                res += isPalindrome(s, l, r)
        
        return res
            
            
class Solution:
    def countSubstrings(self, s: str) -> int:  
        res = 0
        for i in range(len(s)):
            res += self.palindrome(s, i, i)
            res += self.palindrome(s, i, i+1)
            
        return res

    def palindrome(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        return res