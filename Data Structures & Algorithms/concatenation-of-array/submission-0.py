class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            # place 1 on ans array 2x size on 0, 3
            # place 2 on ans array 2x size on 1, 4
            # repeat....
            ans[i] = ans[i + n] = num
        return ans

        