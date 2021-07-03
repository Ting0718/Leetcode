def romanToInt(self, s: str) -> int:
    n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    special = {"IV": 4, "XL": 40, "CD": 400, "IX": 9, "XC": 90, "CM": 900}
    total = 0
    index = 0

    while index < len(s):
        if index + 1 < len(s):
            if s[index] + s[index+1] in special.keys():
                total += special[s[index] + s[index+1]]
                index += 2
            else:
                total += n[s[index]]
                index += 1
        else:
            total += n[s[index]]
            index += 1

    return total

# Better Solution
    def romanToInt(s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        for i in s:
            number += d[i]

        return number
