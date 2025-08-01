class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        col = cols - 1
        row = 0

        while row < rows and col >= 0:
            if target ==matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col = col - 1
            else:
                row = row + 1
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        