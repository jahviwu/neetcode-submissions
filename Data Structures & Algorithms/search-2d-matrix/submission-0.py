class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])  
        topRow, botRow = 0, rows - 1

        while topRow <= botRow:
            midRow = (topRow + botRow) // 2
            if target > matrix[midRow][-1]: # if target is greater than the last value in the row
                topRow = midRow + 1
            elif target < matrix[midRow][0]: # if target is less than the first value in the row
                botRow = midRow - 1
            else:
                break # Will always breaks once it finds a row (or not)

        # if target is too big or small for each row's range no matter how many times we shift the top and bottom rows, 
        # it obviously does not exist in the 2d matrix 
        if not (topRow <= botRow): 
            return False 
        
        # Binary Search within the row we are in
        midRow = (topRow + botRow) // 2 
        l, r = 0, cols - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[midRow][m]: # if target is greater than "our row's m'th value" Ex. [4, 3, 6, 7] in this row, m would be like 3 
                l = m + 1
            elif target < matrix[midRow][m]:
                r = m - 1
            else:
                return True
        
        # if we never found the target
        return False