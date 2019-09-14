class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrixLength = len(matrix)
        if(matrixLength == 1):
            return matrix
        for i in range(0, matrixLength // 2 + matrixLength % 2):
            for j in range(0, matrixLength // 2):
                row = i
                column = j
                tmp = matrix[row][column]
                for k in range(4): #move counterclockwise
                    if k == 3: #moving the final point of the four
                        matrix[row][column] = tmp
                    else:
                        matrix[row][column] = matrix[matrixLength-1-column][row]
                        row, column = matrixLength-1-column, row

        
