class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int)-> bool:
        print("target:", target)
        # Searching for the right row
        upper = len(matrix) - 1
        lower = 0
        
        while lower <= upper: # Using target as stopping condition causedindex error inevitably
            row = (upper + lower) //2
            
            if matrix[row][0] <= target:
                lower = row + 1 # Lower increases at target row till lower > Upper
            else:
                upper = row -1 # Always stops decrementing at target row
        row = upper
            
        
        # Searching inside row
        upper = len(matrix[row]) - 1
        lower = 0

        while (lower <= upper): 
            pred = (upper + lower) //2  
            
            if matrix[row][pred] <= target:
                lower = pred + 1
            else:
                upper = pred - 1
        
        pred = upper
        
        if matrix[row][pred] != target:
            return False
        else:
            return True
