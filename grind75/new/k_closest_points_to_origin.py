from typing import List

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = (0-x)**2 + (0-y)**2
            minHeap.append([dist,x,y])
        
        heapq.heapify(minHeap)
        res = []
        while len(res) < k:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])

        return res

    # NOTE: THIS IS NOT THE INTENDED SOLUTION - THIS IS A MIN HEAP PROBLEM
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {} #distance from origin : [points]
        res = []

        for p in points:
            # don't need to compute sqrt
            dist = (0-p[0])**2 + (0-p[1])**2
            if dist in distances:
                distances[dist].append(p)
            else:
                distances[dist] = [p]
        
        orderedDistances = sorted(distances.keys())
        for od in orderedDistances:
            for val in distances[od]:
                res.append(val)
                if len(res) == k:
                    return res
        return res 