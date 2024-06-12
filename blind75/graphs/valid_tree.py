from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        # create adjacency list for each node
        adj = {i:[] for i in range(n)}
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        # return (no cycles in graph) and (num nodes traversed = total num nodes (i.e. no disconnected nodes))
        return self.dfs(0, -1, adj, visited) and n == len(visited)
        
    
    def dfs(self, i, prev, adj, visited):
        # cycle detected, return false
        if i in visited:
            return False
        
        visited.add(i)
        # explore connected nodes
        for j in adj[i]:
            # skip node we just connected from
            if j == prev:
                continue
            if not self.dfs(j, i, adj, visited):
                return False

        # traversed graph, no cycles detected, return true
        return True