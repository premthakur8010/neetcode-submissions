class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        cur = []

        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return

            # Take nums[i]
            cur.append(nums[i])
            dfs(i + 1)

            # Don't take nums[i]
            cur.pop()

            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)
        return res