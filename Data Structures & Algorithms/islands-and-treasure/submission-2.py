class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def addcell(r, c):
            # check valid steps
            if (
                min(r,c) < 0
                or r == rows
                or c == cols
                or (r,c) in visited
                or grid[r][c] == -1
            ):
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
            
        dist = 0
        # first in first out: first in(closest to treasure) then last in(furthest to treasure)
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addcell(r+1, c)
                addcell(r-1, c)
                addcell(r, c-1)
                addcell(r, c+1)
            dist += 1


       