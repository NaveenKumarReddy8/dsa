class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # -4, -1, -1, 0, 1, 2
        result = set()
        length = len(nums)

        for index in range(length - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue  # Skip duplicate starting numbers
            if nums[index] > 0:
                return list(result)
            left = index + 1
            right = length - 1

            while left < right:
                total = nums[index] + nums[left] + nums[right]
                if total == 0:
                    result.add(tuple(sorted((nums[index], nums[left], nums[right]))))
                    # Move both pointers to find other potential triplets
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return list(result)
