import collections

class Solution(object):
    
    # want to avoid sorting each string, use bucket sort to represent each string
    # O(m * n), m = num words, n = avg len of words
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            bucket = [0] * 26
            for c in word:
                bucket[ord(c) - ord('a')] += 1
            
            anagrams[tuple(bucket)].append(word)
        
        return anagrams.values()
     
    # map anagrams by sorted word, O(m * nlogn)
    # m = num words, n = avg len of words
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagrams = {}
        
        for word in strs:
            ordered = ('').join(sorted(word))
            if ordered in anagrams:
                anagrams[ordered].append(word)
            else:
                anagrams[ordered] = [word]
        
        return [value for value in anagrams.values()]