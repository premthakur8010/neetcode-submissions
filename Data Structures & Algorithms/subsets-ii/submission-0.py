class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def backtrack():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for num in nums:
                if num in cur:
                    continue

                cur.append(num)

                backtrack()

                cur.pop()

        backtrack()
        return res