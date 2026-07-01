class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        
        for i,n in enumerate(nums):
            ind[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in ind and ind[diff] != i:
                return [i,ind[diff]]
        return []