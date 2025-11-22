class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # Pythonic
        # return len(nums) != len(set(nums))

        # Hashing
        seen = set()
        for value in nums:
            if value in seen:
                return True
            seen.add(value)
        return False
