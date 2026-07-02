class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        res = nums[0]
        while left<=right:
            if nums[left]<nums[right]:
                res = min(res,nums[left])
                break
            m = (left+right)//2
            res = min(res, nums[m])
            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1
            res = min(res, nums[m])
        return res


        