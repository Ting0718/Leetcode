class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:  # empty Tree
            return True

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:  # undirected, so both way
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:  # detect a cyle
                return False
            visit.add(i)
            for nei in adj[i]:
                if nei == prev:  # visited neighbor will trigger detecting a loop, not calling dfs on the prev neigbor
                    continue

                if not dfs(nei, i):  # detect a cycle
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
