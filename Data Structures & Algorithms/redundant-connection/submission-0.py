class Solution:
    def findRedundantConnection(self, edges):
        graph = [[] for _ in range(len(edges) + 1)]

        def dfs(node, target, visited):
            if node == target:
                return True

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour, target, visited):
                        return True

            return False

        for a, b in edges:
            visited = set()

            if dfs(a, b, visited):
                return [a, b]

            graph[a].append(b)
            graph[b].append(a)

        return []