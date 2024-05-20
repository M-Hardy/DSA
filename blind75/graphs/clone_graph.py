# *review bfs solution and implement dfs solution for practice

from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        
        cloned = {node.val: Node(node.val, [])}
        
        def bfs(node):
            q = deque() 
            q.append(node)
            
            while q:
                node = q.popleft()
                clone = cloned[node.val]
                
                for nei in node.neighbors:
                    if nei.val not in cloned:
                        cloned[nei.val] = Node(nei.val, [])
                        q.append(nei)
                    clone.neighbors.append(cloned[nei.val])
                    
        bfs(node)
        return cloned[node.val]