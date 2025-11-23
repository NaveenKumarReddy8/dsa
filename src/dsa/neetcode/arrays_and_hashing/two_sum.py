class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        value_index = dict()
        for idx, value in enumerate(nums):
            diff = target - value
            if diff in value_index:
                return [value_index[diff], idx]
            value_index[value] = idx
