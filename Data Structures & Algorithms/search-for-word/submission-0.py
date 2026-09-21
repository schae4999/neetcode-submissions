class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # locate the first letter in the word
        # from there, check up, down, left right to see if the next letter exists
        # dfs

        # current row index
        # current col index
        # which char in word we're trying to match

        visited = set()

        def backtrack(row, col, index):
            if (row, col) in visited or (board[row][col] != word[index]):
                return False

            if (index == len(word) - 1):
                return True

            visited.add((row, col))

            # up
            if (row > 0):
                if backtrack(row - 1, col, index + 1):
                    return True

            # down
            if (row < len(board) - 1):
                if backtrack(row + 1, col, index + 1):
                    return True

            # left
            if (col > 0):
                if backtrack(row, col - 1, index + 1):
                    return True
            
            # right
            if col < len(board[0]) - 1:
                if backtrack(row, col + 1, index + 1):
                    return True

            visited.remove((row, col))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0):
                    return True
        return False
            
