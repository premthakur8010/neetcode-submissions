from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            n = len(q)

            for i in range(n):
                x = q.popleft()

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

                if i == n - 1:
                    ans.append(x.val)

        return ans