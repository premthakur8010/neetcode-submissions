import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []

        # Add all numbers to the heap
        for num in nums:
            heapq.heappush(self.heap, num)

            # Keep only k largest elements
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add new value
        heapq.heappush(self.heap, val)

        # Remove smallest if heap becomes larger than k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Smallest element is the kth largest
        return self.heap[0]