class Solution(object):
    
    #want to avoid set->list conversion, this is caused by duplicate
    #entries in buckets. we can remove duplicate entries in buckets
    #by adding them from finished counts rather than intermediate counts
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        result = []
        counts = {}
        buckets = [[] for i in range(len(nums) + 1)]  #len+1 because storing counts requires 1-indexing 
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, count in counts.items():
            buckets[count].append(num)
            
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                    
        return list(result)
    
    # M for traversing nums, 26 for traversing buckets, N for avg len of bucket, P len of result set
    # O(M + 26*N + P)
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        result = set()
        counts = {}
        buckets = [[] for i in range(len(nums) + 1)]  #len+1 because storing counts requires 1-indexing 
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            buckets[counts[num]].append(num)
            
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.add(num)
                if len(result) == k:
                    return result
                    
        return list(result)