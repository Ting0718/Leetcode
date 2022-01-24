class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prereqs
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:  # visited twice
                return False
            if crs in visit:  # don't have to visit again
                return True

            cycle.add(crs)
            # running all the crs's prereq
            for preq in preMap[crs]:
                if not dfs(preq):
                    return False

            cycle.remove(crs)  # no longer along the path we are going
            visit.add(crs)
            output.append(crs)  # went through all the crs's prereq
            return True

        for crs in range(numCourses):
            if not dfs(crs):  # detect a cycle
                return []

        return output
