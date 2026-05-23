class MedianFinder:
    # idea is to have two heaps: min-heap and max-heap
    # median is either average of 2 values
    # keep the difference between 1, so odd length, just retrieve either min-h or max-h

    def __init__(self):
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        # push to min-heap or max-heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # if length of small > length of large
        # multiply by -1 to get the value
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        # equal length
        return (-1 * self.small[0] + self.large[0]) / 2.0
        
        