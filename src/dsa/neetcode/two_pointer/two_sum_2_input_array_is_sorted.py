class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            added_value = numbers[left] + numbers[right]
            if added_value == target:
                return [left + 1, right + 1]
            if added_value < target:
                left += 1
            else:
                right -= 1
