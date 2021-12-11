'''recursion'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(i, j, length):
            if i == len(text1) or j == len(text2):
                return length
            
            if text1[i] == text2[j]:
                return lcs(i + 1, j + 1, length + 1)
            
            else:
                return max(lcs(i + 1, j, length), lcs(i, j + 1, length))
        
        
        return lcs(0, 0, 0)


'''dynamic programming'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]  # +1 for a column of 0

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]  # add diagonal value
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]
