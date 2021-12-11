class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        prime = [True for i in range(n)]
        p = 2
        while p*p < n:
            if prime[p] == True:
                for i in range(p*p, n, p):
                    prime[i] = False

            p += 1

        return sum(prime) - 2