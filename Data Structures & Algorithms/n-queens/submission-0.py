class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.' for _  in range(n)] for _ in range(n)]
        cols = set()
        neg_dia = set() # key = (r - c)
        pos_dia = set() # key = (r + c)

        def backtrack(row):
            if row == n:
                result.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in neg_dia or (row + col) in pos_dia:
                    continue
                
                # place the queen
                board[row][col] = 'Q'
                cols.add(col)
                neg_dia.add(row - col)
                pos_dia.add(row + col)

                # recursive to place queens in next row
                backtrack(row + 1)

                # backtrack
                board[row][col] = '.'
                cols.remove(col)
                pos_dia.remove(row + col)
                neg_dia.remove(row - col)


        backtrack(0)
        return result
        