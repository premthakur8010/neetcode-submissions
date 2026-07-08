class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)

        ans = []
        limit = len(nums)//3
        for num,freq in count.items():
            if freq>limit:
                ans.append(num)
        return ans
        