class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        ans = []

        # Can this cell reach the Pacific?
        def canReachPacific(r, c, visited):

            # Reached Pacific (top or left edge)
            if r == 0 or c == 0:
                return True

            visited.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in visited and
                    heights[nr][nc] <= heights[r][c]
                ):
                    if canReachPacific(nr, nc, visited):
                        return True

            return False

        # Can this cell reach the Atlantic?
        def canReachAtlantic(r, c, visited):

            # Reached Atlantic (bottom or right edge)
            if r == ROWS - 1 or c == COLS - 1:
                return True

            visited.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in visited and
                    heights[nr][nc] <= heights[r][c]
                ):
                    if canReachAtlantic(nr, nc, visited):
                        return True

            return False

        for r in range(ROWS):
            for c in range(COLS):

                if (
                    canReachPacific(r, c, set()) and
                    canReachAtlantic(r, c, set())
                ):
                    ans.append([r, c])

        return ans