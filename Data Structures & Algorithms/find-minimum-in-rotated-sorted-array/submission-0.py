class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # execute binary search
            m = (l+r) // 2
            res = min(res, nums[m])

            # middle value in left sorted portion
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # middle value in right sorted portion
                r = m - 1
        return res
        