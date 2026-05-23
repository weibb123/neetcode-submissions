class Solution:
    def rob(self, nums: List[int]) -> int:
        # so we cannot rob first and last houses

        # edge cases
        if len(nums) == 1:
            return nums[0]
        
        # skip first house, [1:], or skip last house
        return max(self.helper(nums[1:]),
                    self.helper(nums[:-1]))
        
    def helper(self, nums):
        prev1, prev2 = 0, 0

        for n in nums:
            curr = max(prev1 + n, prev2)
            prev1, prev2 = prev2, curr
            
        return curr
        