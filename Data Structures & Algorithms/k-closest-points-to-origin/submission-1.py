class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # input: [[0,2],[2,0],[2,2]]
        # compute distance: x^2 + y^2
        # python by default: min-heap, everytime pop, smallest element(closest)
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]