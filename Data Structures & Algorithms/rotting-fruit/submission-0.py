class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                directions = [
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0)
                ]

                for (dr, dc) in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr, nc))

            if queue:
                count += 1

        if fresh > 0:
            return -1
        
        return count
        