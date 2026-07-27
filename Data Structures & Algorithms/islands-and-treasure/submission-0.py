from collections import deque

class Solution:
    def islandsAndTreasure(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        # Put every treasure into the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        # BFS
        while queue:

            r, c = queue.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Skip outside grid
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Only visit INF cells
                if grid[nr][nc] != 2147483647:
                    continue

                # Current distance + 1
                grid[nr][nc] = grid[r][c] + 1

                queue.append((nr,nc))