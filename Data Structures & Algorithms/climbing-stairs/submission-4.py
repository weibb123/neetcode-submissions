class Solution:
    def climbStairs(self, n: int) -> int:
        # each step: I can climb either 1 or 2 steps
        # goal: return number of ways to climb to the top

        # recursion
        # decision tree: DFS
        def dfs(i):
            # base case: exceed top of stairs
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        
        # start at step 0
        return dfs(0)
        # time complexity: O(2^n)
        