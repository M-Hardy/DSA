# LONGEST CONSECUTIVE 1 - write why it is much faster & less memory 
# (why you actually need much less memory and what makes it so much faster)
# determine time complexity of both algorithms (and space if you want)

#LONGEST CONSECUTIVE 2 SOLUTION (original solution - much slower, much more memory)
# note: naming convention for 'starts' and 'ends' is confusing
#       to read (it works for the conditionals but not in the 
#       conditional bodies)

# every number is the start, end, or middle of a sequence (besides new sequences)
# remember the longest length so far, start nums of sequences, and end nums of sequences
# for each number, check if it is start of sequence, end of sequence, or middle of sequence
# update the longest length and new start & end nums

# *skipping already inserted nums: 
#  for each num in the array, the nums adjacent to our current num are checked if 
#  they are the start/end of an already existing sequence, and our new num is added to it. 
#  When a new num is added to a sequence,  the start and end nums of the sequence are 
#  updated (i.e. start is paired with new end, end is paired with new start) so the length
#  of the sequence can be obtained and compared to our maximum length sequence.
#  
#  As a detected sequence gets larger its intermediate values are no longer updated - they 
#  are associated with start/end values from earlier in the sequence's creation, and are not
#  aware of the new start/end values of the sequence. As a result, if you try to update a 
#  number that is already in a sequence (it is repeated in the array), it will use the numbers
#  next to it - which will be intermediate values (one or both) - which will have outdated
#  start/end values associated with it.
#  
#  Note that updating all intermediate values with correct start/end values is not  
#  needed to determine the longest sequence as the start/end values of the sequence are 
#  all that is strictly required.

class Solution(object):
     def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            # get the longest sequence from each num that is the start of a sequence
            if (num-1) not in numSet:
                length = 1
                while (num+length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest
    

     def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        longest_len = 0
        #start:end pairs
        starts = {}
        #end:start pairs
        ends = {}
        
        for num in nums:
            
            #edge case - do not insert num that is already in a sequence (skip it)*
            if num in starts:
                continue
                
            #num is 'sequence joiner' (middle number)
            elif (num-1) in ends and (num+1) in starts:
                l_start = ends[num-1]
                r_end = starts[num+1]
                starts[num] = r_end
                ends[num] = l_start
                starts[l_start] = r_end
                ends[r_end] = l_start
                longest_len = max(longest_len, r_end - l_start + 1)
                
            #num is 'sequence end' (end number)
            elif (num-1) in ends and (num+1) not in starts:
                l_start = ends[num-1]
                starts[num] = num
                ends[num] = l_start
                starts[l_start] = num
                longest_len = max(longest_len, num - l_start + 1)
                
            #num is 'sequence start' (start number)
            elif (num-1) not in ends and (num+1) in starts:
                r_end = starts[num+1]
                starts[num] = r_end
                ends[num] = num
                ends[r_end] = num
                longest_len = max(longest_len, r_end - num + 1)
                
            #num is unconnected, new sequence of len = 1
            else:
                starts[num] = num
                ends[num] = num
                longest_len = max(longest_len, 1)

        return longest_lenn