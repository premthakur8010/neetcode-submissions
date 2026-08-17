from collections import deque, defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the graph and count incoming arrows (prerequisites) per course
        graph = defaultdict(list)       # graph[b] = list of courses that need b first
        indegree = [0] * numCourses     # indegree[x] = how many prerequisites x still needs

        for a, b in prerequisites:
            graph[b].append(a)          # arrow b -> a  ("finishing b unlocks a")
            indegree[a] += 1            # a needs one more prerequisite

        # Step 2: Start with courses that have NO prerequisites (ready right now)
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        taken = 0  # how many courses we've successfully "taken"

        # Step 3: Keep taking ready courses, unlocking new ones as we go
        while queue:
            course = queue.popleft()
            taken += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:   # it just became ready
                    queue.append(next_course)

        # Step 4: If we took every course, there was no cycle
        return taken == numCourses