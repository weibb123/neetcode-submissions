class Solution:
    def climbStairs(self, n: int) -> int:
        # decision tree but with caching
        # initiate a cache array [-1] * n

        # write dfs(i)
        # use cache to avoid computations, bring down to O(n)
        
        # function dfs(i)
        # same base case: cannot exceed top of floor
        # if cache[i] != -1: use the answer
        # store answer in the cache: cache[i] = dfs(i+1) + dfs(i + 2)
        # return cache[i]
        # start dfs(0)
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0) # time complexity/space: O(n)
        
        