
'''Sliding Window'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res

'''Optimized'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        maxFreq = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(count[s[r]], maxFreq)
            
            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res