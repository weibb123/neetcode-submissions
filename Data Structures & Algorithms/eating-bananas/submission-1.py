class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search: what are we searching?
        # we are searching for k, eating rate.
        # cannot exceed h
        # get the skeleton of BS
        # start with maximum piles, then decrease it and see if we can still finish on time
        l, r = 1, max(piles)
        # current initial non-optimal solution
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                # record current solution
                res = k
                # find a smaller solution
                r = k - 1
            # cannot finish on time
            else:
                l = k + 1
        return res


        