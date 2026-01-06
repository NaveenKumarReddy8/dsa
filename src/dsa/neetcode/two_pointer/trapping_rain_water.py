class Solution:
    def trap(self, height: list[int]) -> int:
        length = len(height)
        if length <= 2:
            return 0

        prefix_max_array = [0] * length
        prefix_max_array[0] = height[0]
        suffix_max_array = [0] * length
        suffix_max_array[length - 1] = height[length - 1]
        for i in range(1, length):
            prefix_max_array[i] = max(prefix_max_array[i - 1], height[i])
            suffix_max_array[length - 1 - i] = max(
                suffix_max_array[length - i], height[length - 1 - i]
            )
        return sum(
            (
                min(prefix_max_array[i], suffix_max_array[i]) - height[i]
                for i in range(1, length - 1)
            )
        )
