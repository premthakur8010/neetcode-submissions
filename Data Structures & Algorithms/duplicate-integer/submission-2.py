class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return True
        return False