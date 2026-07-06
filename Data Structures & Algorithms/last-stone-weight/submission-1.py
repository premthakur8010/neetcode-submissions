import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Convert all values to negative
        for i in range(len(stones)):
            stones[i] = -stones[i]

        # Create a max heap
        heapq.heapify(stones)

        while len(stones) > 1:

            # Two largest stones
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            # If they are different
            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0

        