class Solution(object):
    def findComplement(self, num):
        binary = ""
        while num:
            binary = str(num & 1) + binary
            num = num >> 1

        dec = 0
        for i in range(len(binary)):
            if binary[::-1][i] == "0":
                dec += 2**i

        return dec


class Solution(object):
    def findComplement(self, num):
        bit = 1
        while num >= bit:
            num ^= bit
            bit <<= 1

        return num
