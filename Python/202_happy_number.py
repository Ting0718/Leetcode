class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n != 1:
            tmp = 0
            for i in range(len(str(n))):
                tmp += int(str(n)[i])**2
            n = tmp
            if n in visit:
                return False
            else:
                visit.add(n)

        return True




