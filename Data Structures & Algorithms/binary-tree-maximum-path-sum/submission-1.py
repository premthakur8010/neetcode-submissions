class Solution:
    def maxPathSum(self, root):
        ans = float('-inf')

        def dfs(n):
            nonlocal ans

            if not n:
                return 0

            l = max(0, dfs(n.left))
            r = max(0, dfs(n.right))

            ans = max(ans, n.val + l + r)

            return n.val + max(l, r)

        dfs(root)
        return ans