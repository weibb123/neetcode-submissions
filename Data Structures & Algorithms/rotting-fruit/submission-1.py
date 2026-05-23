class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # initialize
        q = deque()
        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # check valid boundary
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2 # set to rotten
                        q.append((row,col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

                    

        
        