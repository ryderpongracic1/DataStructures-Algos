# Dependency Cycle Detection - DFS
# sets: visited - full dependency safe, visiting - cycle detected
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = collections.defaultdict(list) # crs -> prereqs
        for p1, p2 in prerequisites:
            prereqs[p1].append(p2)

        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting: # cycle
                return False
            visiting.add(crs)
            for p in prereqs[crs]:
                if not dfs(p):
                    return False
            visiting.remove(crs) # fully cleared
            visited.add(crs)
            return True

        for crs in range(numCourses):
            if crs not in visited:
                if not dfs(crs):
                    return False
        return True