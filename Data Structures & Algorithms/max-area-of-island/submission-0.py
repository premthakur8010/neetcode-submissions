class Solution:
    def maxAreaOfIsland(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        maxArea = 0

        def dfs(r,c):

            # Outside grid or water
            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                grid[r][c] == 0
            ):
                return 0

            # Mark visited
            grid[r][c] = 0

            # Count this cell
            area = 1

            # Add areas of neighbouring cells
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(maxArea, area)

        return maxArea
        