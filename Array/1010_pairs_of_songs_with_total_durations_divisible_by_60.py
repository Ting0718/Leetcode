'''Brute Force'''
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        count = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        
        return count

from collections import defaultdict
'''use modulo formula'''
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        remainders = defaultdict(int)
        res = 0
        for t in time:
            if t % 60 == 0:
                res += remainders[0]
            else:
                res += remainders[60-t % 60]

            remainders[t % 60] += 1

        return res
