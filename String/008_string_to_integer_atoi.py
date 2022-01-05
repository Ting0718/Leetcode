class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = "+"
        n = 0
        for i in range(len(s)):
            if i == 0 and (s[i] == "+" or s[i] == "-"):
                sign = s[i]
            elif s[i].isnumeric():
                n = n * 10 + int(s[i])
            else:
                break

        if sign == "-":
            n = -n

        if n < -2**31:
            return -2**31
        if n > 2**31 - 1:
            return 2**31 - 1
        else:
            return n
