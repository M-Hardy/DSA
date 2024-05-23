from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = 0

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            res = max(cur, res)
        return res

    def maxSubArray2(self, nums: List[int]) -> int:
        res = cur = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                res = max(cur, res)

                if cur + nums[i] > 0:
                    cur += nums[i]
                else: 
                    cur = nums[i]
            else:
                if cur < 0:
                    cur = nums[i]
                else:
                    cur += nums[i]                 

        return max(res, cur)
