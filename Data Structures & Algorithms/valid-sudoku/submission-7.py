class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each row
        for row in board:
            seen = set()
            for val in row:
                if val == ".":
                    continue
                elif val in seen:
                    return False
                else:
                    seen.add(val)

        #check each col
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        #check each 3x3 grid
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()

                for row in range(i, i+3):
                    for col in range(j, j+3):
                        val = board[row][col]
                        if val in seen:
                            return False
                        if val != ".":
                            seen.add(val)

        return True
        