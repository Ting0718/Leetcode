'''bfs solution'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = [(r, c)]
            visited.add((r,c))
            while queue:
                r, c = queue.pop(0)
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        return islands