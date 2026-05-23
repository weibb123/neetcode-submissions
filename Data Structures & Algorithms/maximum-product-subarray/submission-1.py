class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # this DP problem uses answer from previous state to find ans of current state
        curMin, curMax = 1, 1
        res = nums[0]
        for n in nums:
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        
        return res

        
        