class Solution(object):
    def minKnightMoves(self, x, y):
        visited = {(0, 0)}
        queue = [(0, 0)]
        steps = 0
        directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        while queue:
            for i in range(len(queue)):
                x1, y1 = queue.pop(0)
                if x1 == abs(x) and y1 == abs(y):
                    return steps

                for dx, dy in directions:
                    nx, ny = dx + x1, dy + y1
                    if (nx, ny) not in visited and nx >= -2 and ny >= -2:
                        queue.append((nx, ny))
                        visited.add((nx, ny))

            steps += 1

        return steps
