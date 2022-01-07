class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # new interval not overlapping
                res.append(newInterval)
                return res + intervals[i:] # all the intervals come after i are not overlapped
            elif newInterval[0] > intervals[i][1]: # newInterval is after intervals[i
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res