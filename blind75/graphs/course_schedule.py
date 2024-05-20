from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        explored = set()
        for c in range(numCourses):
            visited = set()
            if not self.dfs(c,prerequisites,visited,explored):
                return False
        return True
    
    def dfs(self, c, prereqs, visited,explored):
        if c in visited:
            return False
        if c in explored:
            return True
        
        visited.add(c)
        for p in prereqs:
            if c == p[0] and not self.dfs(p[1], prereqs, visited,explored):
                return False
        explored.add(c)
        visited.remove(c)
        return True   