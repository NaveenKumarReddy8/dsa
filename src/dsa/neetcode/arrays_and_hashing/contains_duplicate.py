class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # Pythonic
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # return len(nums) != len(set(nums))

        # Generic
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
