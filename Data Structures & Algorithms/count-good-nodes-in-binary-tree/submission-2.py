class Solution:
    def goodNodes(self, root):
        def dfs(node, maxval):
            if not node:
                return 0

            count = 0

            if node.val >= maxval:
                count = 1

            maxval = max(maxval, node.val)

            return count + dfs(node.left, maxval) + dfs(node.right, maxval)

        return dfs(root, root.val)