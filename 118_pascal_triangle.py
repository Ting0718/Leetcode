class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(array):
            if len(array) == 1:
                return [1, 1]
            if len(array) == 2:
                return [1, 2, 1]
            else:
                l = []
                for i in range(len(array)):
                    if array[i] == 1:
                        l.append(array[i])
                    if i < len(array) - 1:
                        l.append(array[i] + array[i + 1])
            return l

        res = [[1]]
        for i in range(numRows-1):
            res.append(helper(res[i]))

        return res
