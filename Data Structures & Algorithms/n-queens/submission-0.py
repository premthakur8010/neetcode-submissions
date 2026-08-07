class Solution:
    def solveNQueens(self, n: int):

        board = [["."] * n for _ in range(n)]
        ans = []

        def isSafe(row, col):

            # Check column
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            # Check left diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Check right diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def dfs(row):

            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):

                if isSafe(row, col):

                    board[row][col] = "Q"

                    dfs(row + 1)

                    board[row][col] = "."

        dfs(0)
        return ans