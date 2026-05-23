class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        # we know if n = 1, we have 1 way to climb stairs
        dp[1] = 1
        # we know if n = 2, we have 2 ways to climb stairs
        dp[2] = 2
        # starting from 3, subproblem(3) depends on the solution of dp[1] and dp[2]
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n] # n is the original problem


        