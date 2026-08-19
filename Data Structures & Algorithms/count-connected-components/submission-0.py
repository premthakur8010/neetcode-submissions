class Solution:
    def countComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count