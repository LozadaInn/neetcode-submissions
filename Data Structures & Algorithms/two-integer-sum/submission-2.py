class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in set:
                return [set[rest], i]
            set[num] = i
        return