class Solution:
    def numberToWords(self, num: int) -> str:
        def one(num):
            d = {1: "One",
                 2: "Two",
                 3: "Three",
                 4: "Four",
                 5: "Five",
                 6: "Six",
                 7: "Seven",
                 8: "Eight",
                 9: "Nine"}
            return d.get(num)

        def two_less_20(num):
            d = {10: "Ten",
                 11: "Eleven",
                 12: "Twelve",
                 13: "Thirteen",
                 14: "Fourteen",
                 15: "Fifteen",
                 16: "Sixteen",
                 17: "Seventeen",
                 18: "Eighteen",
                 19: "Nineteen"}
            return d.get(num)

        def ten(num):
            d = {2: "Twenty",
                 3: "Thirty",
                 4: "Forty",
                 5: "Fifty",
                 6: "Sixty",
                 7: "Seventy",
                 8: "Eighty",
                 9: "Ninety"}
            return d.get(num)

        def two(num):
            if not num:
                return ""
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                if not rest:
                    return ten(tenner)
                else:
                    return ten(tenner) + " " + one(rest)

        def three(num):
            if not num:
                return ""

            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + " Hundred " + two(rest)
            elif hundred and not rest:
                return one(hundred) + " Hundred"
            else:
                return two(rest)

        if not num:
            return "Zero"

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        res = ""
        if billion:
            res = res + three(billion) + " Billion"

        if million:
            if res:
                res += " "
            res = res + three(million) + " Million"

        if thousand:
            if res:
                res += " "
            res = res + three(thousand) + " Thousand"

        if rest:
            if res:
                res += " "

            res += three(rest)

        return res