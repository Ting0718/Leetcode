class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = 0
        for i in range(len(columnTitle)):
            s += (ord(columnTitle[::-1][i]) - ord("A") + 1) * 26**i

        return s
