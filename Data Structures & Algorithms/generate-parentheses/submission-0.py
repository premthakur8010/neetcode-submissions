class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def backtrack(open, close):
            if open == close == n:
                res.append("".join(cur))
                return

            if open < n:
                cur.append("(")
                backtrack(open + 1, close)
                cur.pop()

            if close < open:
                cur.append(")")
                backtrack(open, close + 1)
                cur.pop()

        backtrack(0, 0)
        return res