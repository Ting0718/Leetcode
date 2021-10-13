class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # breath first search -> minimum search
        x = abs(x)
        y = abs(y)
        moves = 0
        visited = {"0,0"}

        queue = [[0, 0]]

        xdir = [-2, -2, -1, -1, 1, 1, 2, 2]
        ydir = [-1,  1, -2,  2, -2, 2, -1, 1]

        while queue:
            size = len(queue)
            for i in range(size):
                point = queue.pop(0)
                if point[0] == x and point[1] == y:
                    return moves
                for j in range(len(xdir)):
                    new_px = point[0] + xdir[j]
                    new_py = point[1] + ydir[j]
                    point_s = str(new_px) + "," + str(new_py)
                    if point_s not in visited and new_px >= -2 and new_py >= -2:
                        queue.append([new_px, new_py])
                        visited.add(point_s)
            moves += 1
