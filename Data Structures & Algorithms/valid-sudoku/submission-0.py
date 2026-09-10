class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
   
        # Storage
        col_tracker : dict[int, set[str]] = {} # Tracks every column separately

        for i, row in enumerate(board):
            row_tracker : set[str] = set() # Reset row tracker every row
            if i == 0 or i == 3 or i == 6: # Reset boxes every 3 rows
                box1 : set[str] = set()
                box2 : set[str]= set()
                box3 : set[str]= set()

            for j, val in enumerate(row):
                if val != ".":
                    #9x9 check
                    if val in row_tracker: # Check for duplicates in row
                        return False
                    else:
                        row_tracker.add(val)
                    
                    if j not in col_tracker: # Use get to prevent keyerror
                        col_tracker[j] = set()
                    if val in col_tracker[j]:
                        return False
                    else:
                        col_tracker[j].add(val)
                    # Sub-box check
                    if j <= 2: # first box
                        if val in box1:
                            return False
                        else:
                            box1.add(val)
                        
                    if j > 2 and j <= 5: # Middle boxes
                        if val in box2:
                            return False
                        else:
                            box2.add(val)
                    if j > 5: # third box
                        if val in box3:
                            return False
                        else:
                            box3.add(val)
        return True


      

