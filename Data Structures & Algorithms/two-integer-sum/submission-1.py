class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            rest = target - num
            if rest in nums and nums.index(rest) != i:
                return sorted([i, nums.index(rest)])