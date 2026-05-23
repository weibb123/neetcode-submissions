class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # base case
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            # add value
            dfs(i, cur, total + nums[i])
            cur.pop()
            # skip add value
            dfs(i+1, cur, total)
        
        # dfs on initial index, [], total=0
        dfs(0, [], 0)
        return res


        