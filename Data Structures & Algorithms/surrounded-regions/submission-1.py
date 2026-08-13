class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != 'O'):
                return

            # Mark this O as safe
            board[r][c] = 'S'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Find all O's on the border

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)

            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)

            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        # 2. Capture surrounded O's
        # 3. Restore safe O's

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == 'O':
                    board[r][c] = 'X'

                elif board[r][c] == 'S':
                    board[r][c] = 'O'