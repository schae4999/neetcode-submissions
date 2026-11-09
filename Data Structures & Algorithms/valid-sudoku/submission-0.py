class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for row in range(n):
            seen = set()

            for i in range(n):
                if board[row][i] == ".":
                    continue

                if board[row][i] in seen:
                    return False
                
                seen.add(board[row][i])
        
        for col in range(n):
            seen = set()

            for i in range(n):
                if board[i][col] == ".":
                    continue

                if board[i][col] in seen:
                    return False
                
                seen.add(board[i][col])

        # 0, 3, 6
        for r in range(0, n, 3):
            # 0, 3, 6
            for c in range(0, n, 3):
                seen = set()

                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] == ".":
                            continue

                        if board[r + i][c + j] in seen:
                            return False
                        
                        seen.add(board[r + i][c + j])

        return True
