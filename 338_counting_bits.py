class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            l.append(int(self.toBin(i).count("1")))
        return l

    def toBin(self, n: int) -> int:
        quotient = n // 2
        remainder = n % 2
        bit = str(remainder)
        while quotient > 0:
            remainder = quotient % 2
            quotient = quotient // 2
            bit += str(remainder)

        return bit[::-1]


class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []

        def toBin(n: int):
            quotient = n // 2
            remainder = n % 2
            bit = str(remainder)
            while quotient > 0:
                remainder = quotient % 2
                bit += str(remainder)
                quotient = quotient // 2
            return bit[::-1].count("1")

        for i in range(n+1):
            l.append(toBin(i))

        return l
