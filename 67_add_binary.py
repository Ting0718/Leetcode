
'''
the first solution
'''


def bin_to_dec(a):
    dec_a = 0
    a1 = list(a)[::-1]
    for i in range(len(a1)-1, 0-1, -1):
        if a1[i] == "1":
            dec_a += 2**i
    return dec_a


def addBinary(a: str, b: str) -> str:
    dec = bin_to_dec(a) + bin_to_dec(b)

    binary = ""
    quotient = dec
    while quotient > 0:
        remainder = quotient % 2
        quotient = quotient // 2
        binary += str(remainder)
    return binary[::-1]


print(bin_to_dec("0"))
print(addBinary("1010", "1011"))


'''
convert bin to dec and convert dec back to bin
'''


'''
the second solution
'''
a = "1011"
b = "1010"
print()

