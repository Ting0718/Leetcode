class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        visited = {(0, 0)}
        queue = [(0, 0)]
        moves = 0

        xdir = [-2, -2, -1, -1, 1, 1, 2, 2]
        ydir = [-1,  1, -2,  2, -2, 2, -1, 1]

        while queue:
            for i in range(len(queue)):
                point = queue.pop(0)
                if point[0] == x and point[1] == y:
                    return moves

                for j in range(len(xdir)):
                    nx = xdir[j] + point[0]
                    ny = ydir[j] + point[1]

                    if (nx, ny) not in visited and nx >= -2 and ny >= -2:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

            moves += 1
