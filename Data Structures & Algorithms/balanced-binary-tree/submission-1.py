class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1

            return 1 + max(l,r)

        return dfs(root) != -1