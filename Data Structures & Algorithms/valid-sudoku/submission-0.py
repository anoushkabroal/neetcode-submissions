class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        boxes = []

        for i in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                val = board[row][col]
                boxIndex = (row//3)*3 + (col//3)

                if val in rows[row] or val in cols[col] or val in boxes[boxIndex]:
                    return False

                rows[row].add(val) 
                cols[col].add(val) 
                boxes[boxIndex].add(val) 
        
        return True