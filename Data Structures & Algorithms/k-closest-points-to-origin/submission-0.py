class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create minHeap
        minHeap = []
        # iterate through points with for loop
        for x, y in points:
            # compute distance
            dist = (x**2) + y**2
            # append to minHeap
            minHeap.append([dist, x, y])

        # heapify it
        heapq.heapify(minHeap)
        # have a list to store answer
        res = []
        # while k > 0
        while k > 0:
            # pop dist, x, y from heap -> smallest
            dist, x, y = heapq.heappop(minHeap)
            # append to result
            res.append([x, y])
            # decrement k
            k -= 1
        # return answer arr  
        return res