class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # hand-writing transpose by hand
        n = len(matrix) # since square matrix same

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # step 2 reverse the row
        for i in range(n):
            matrix[i].reverse()

        