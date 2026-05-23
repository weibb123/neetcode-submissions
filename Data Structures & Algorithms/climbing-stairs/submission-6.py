class Solution:
    def climbStairs(self, n: int) -> int:
        # DP: think it from base cases, at top of stairs
        if n <= 2:
            return n
        
        # compute dp array to store answers
        # dp = [0] * (n + 1) for extra space
        dp = [0] * (n+1)
        # prefill dp[1], dp[2] to be our base cases
        dp[1], dp[2] = 1, 2
        # starting 3 all the way to (n+1), relies on answer from previous steps
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        # dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]


        
        