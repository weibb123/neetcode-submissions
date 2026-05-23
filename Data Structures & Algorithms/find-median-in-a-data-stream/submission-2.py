class MedianFinder:

    # recognize that we need two heaps.
    # minHeap, maxHeap, heap should always be equal size
    def __init__(self):
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        # maxHeap, add num to top of heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1*num)
        
        # if len of minHeap > maxHeap
        # pop from minHeap -> add to maxHeap
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # vice versa
        # idea is to maintain difference of 1
        elif len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
        
        