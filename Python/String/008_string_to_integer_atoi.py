class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = "+"
        n = ""
        for i in range(len(s)):
            if i == 0 and (s[i] == '-' or s[i] == '+'):
                sign = s[i]
            elif s[i].isnumeric():
                n += s[i]
            else:
                break

        if n == "" or not n.isnumeric():
            return 0

        else:
            n = int(sign + n)
            if n < -2**31:
                return -2**31
            elif n >= 2**31:
                return 2**31 - 1
            else:
                return n
