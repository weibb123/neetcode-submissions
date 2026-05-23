class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0

        for num in nums:
            curr = max(num + prev1, prev2)
            prev1, prev2 = prev2, curr # shift and update answers
        
        return curr
        