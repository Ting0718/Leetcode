class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(m*n), O(1)
        res = []
        left, right = 0, len(matrix[0])  # make right out of bound
        top, bottom = 0, len(matrix)  # make bottom out of bound

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # shifting top down

            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])  # right is out of bound
            right -= 1  # shifting to the right

            if not (left < right and top < bottom):
                break  # if the column or row == 1

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # shift bottom upwards

            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # shifting left to the right

        return res
