class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        value_index = dict()
        for idx, value in enumerate(nums):
            diff = target - value
            if diff in value_index:
                return [value_index[diff], idx]
            value_index[value] = idx
