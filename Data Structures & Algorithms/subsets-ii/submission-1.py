class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # sort it so can find duplicates easier
        nums.sort()
        res = []
        def backtrack(i, subset):
            # create a deep copy
            res.append(subset[::])

            for j in range(i, len(nums)):
                # spot duplicates
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                backtrack(j + 1, subset) # next index
                subset.pop() # pop to explore other subset
        
        backtrack(0, [])
        return res
        
        