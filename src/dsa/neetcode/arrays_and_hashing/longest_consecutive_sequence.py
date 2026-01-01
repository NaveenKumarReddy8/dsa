class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            count = 1
            current = num
            while current + 1 in nums_set:
                current += 1
                count += 1
            longest = max(count, longest)
        return longest
