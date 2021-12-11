'''Solution: Brute Force (Time Limit Exceeded)'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                chars[ord(s[i])] += 1
                if chars[ord(s[i])] > 1:
                    return False                    
            return True
        
        
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if check(i, j):
                    res = max(res, j - i + 1)
        
        return res

'''from collections import defaultdict'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        current_str = ""
        max_count = 0
        
        for i in range(len(s)):
            if s[i] not in current_str:
                current_str += s[i]
            else:
                current_str = s[d[s[i]] + 1: i + 1]
            
            d[s[i]] = i
            max_count = max(max_count, len(current_str))
        
        return max_count

'''Sliding Window'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 # left pointer
        res = 0
        
        for r in range(len(s)): # right pointer
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res

