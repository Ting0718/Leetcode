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


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for i in range(num_rows):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

            triangle.append(row)

        return triangle
