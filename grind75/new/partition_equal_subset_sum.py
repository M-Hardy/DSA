# key to solution is realizing that if there
# is one subset that == half the sum, then by 
# definition the remaining elements must ALSO
# == half the sum. so the problem is really about
# finding a (single) subset that ==  half the sum; 

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        # odd sum cannot be split into 2 halves
        if sumNums % 2:
            return False
        
        dp = set()
        dp.add(0)

        # for each num, calculate all subarray
        # sums so far using previous subarray
        # sums (dp component)
        for n in nums:
            newDP = set()
            for subSum in dp:
                newDP.add(subSum)
                newDP.add(subSum + n)
                if sumNums // 2 in newDP:
                    return True
            dp = newDP

        return False
      
    # fails
    # test case: [2,2,1,1]
    # don't think my solution will work for odd targets
    # (target == sum array // 2)
    def canPartition2(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        i = 0
        j = len(nums) - 1
        first = nums[i]
        second = nums[j]

        while i < j:

            if i == j-1:
                return first == second

            if first < second:
                i += 1
                first += nums[i]
            
            else:
                j -= 1
                second += nums[j]
        
        return False