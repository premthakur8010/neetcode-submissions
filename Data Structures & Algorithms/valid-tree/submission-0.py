class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()

        def dfs(x):
            seen.add(x)

            for y in graph[x]:
                if y not in seen:
                    dfs(y)

        dfs(0)

        return len(seen) == n