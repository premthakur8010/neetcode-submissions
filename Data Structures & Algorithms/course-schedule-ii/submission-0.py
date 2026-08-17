from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        ans = []

        while queue:
            course = queue.popleft()
            ans.append(course)

            for nextcourse in graph[course]:
                indegree[nextcourse] -= 1

                if indegree[nextcourse] == 0:
                    queue.append(nextcourse)

        if len(ans) == numCourses:
            return ans

        return []