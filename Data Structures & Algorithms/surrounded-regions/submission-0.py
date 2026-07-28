class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):

            # Outside the board
            if (
                r < 0 or
                c < 0 or
                r == ROWS or
                c == COLS
            ):
                return

            # Stop if it's not an 'O'
            if board[r][c] != "O":
                return

            # Mark as safe
            board[r][c] = "T"

            # Explore all four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # DFS from the left and right borders
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        # DFS from the top and bottom borders
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        # Flip surrounded regions and restore safe regions
        for r in range(ROWS):
            for c in range(COLS):

                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "T":
                    board[r][c] = "O"
                    