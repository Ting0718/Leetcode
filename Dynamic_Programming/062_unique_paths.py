class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n  # bottom row
        for i in range(m - 1):
            newRow = [1] * n  # above row
            for j in range(n - 2, -1, -1):  # right most column always be 1
                newRow[j] = newRow[j + 1] + row[j]  # right + below

            row = newRow

        return row[0]
