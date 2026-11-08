class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])

        def dfs(row, col, visited):
            if row >= ROW or col >= COL or row < 0 or col < 0:
                return

            if (row, col) in visited:
                return

            visited.add((row, col))

            # if neighboring height is higher, move to that
            
            if col + 1 < COL and heights[row][col + 1] >= heights[row][col]:
                dfs(row, col + 1, visited)
            if col - 1 >= 0 and heights[row][col - 1] >= heights[row][col]:
                dfs(row, col - 1, visited)
            if row - 1 >= 0 and heights[row - 1][col] >= heights[row][col]:
                dfs(row - 1, col, visited)
            if row + 1 < ROW and heights[row + 1][col] >= heights[row][col]:
                dfs(row + 1, col, visited)
            

        pacific = set()
        atlantic = set()

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                # from pacific, which cells can I go to?
                if row == 0 or col == 0:
                    dfs(row, col, pacific)
                # from atlantic, which cells can I go to?
                if row == ROW - 1 or col == COL - 1:
                    dfs(row, col, atlantic)

        res = []
        for coord in pacific:
            if coord in atlantic:
                res.append(coord)

        return res
                    