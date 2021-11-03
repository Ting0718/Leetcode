class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = {}
        max_year = max_population = 0
        for start, end in logs:
            for y in range(start, end):
                years[y] = years.get(y, 0) + 1
                if years[y] > max_population or (years[y] == max_population and y < max_year):
                    max_year = y
                    max_population = years[y]

        return max_year
