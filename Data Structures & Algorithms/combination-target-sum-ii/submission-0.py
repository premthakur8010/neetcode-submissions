class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        cur = []

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # Take candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            # Backtrack
            cur.pop()

            # Don't take candidates[i]
            # Skip all duplicates of candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, total)

        dfs(0, 0)
        return res