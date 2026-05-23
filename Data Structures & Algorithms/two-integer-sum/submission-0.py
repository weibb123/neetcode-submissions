class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find the indices of i and j such that nums[i] + nums[j] == target
        # i != j
        # for each num we find the difference.
        # save that difference in the hashmap.
        hashmap = {} # 'num': indice

        for i, num in enumerate(nums):
            if (target - num) in hashmap:
                return [hashmap[target-num], i]
            hashmap[num] = i

        