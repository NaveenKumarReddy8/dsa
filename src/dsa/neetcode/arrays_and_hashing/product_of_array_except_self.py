class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length_of_nums = len(nums)
        prefix_product_array = [0] * length_of_nums
        suffix_product_array = [0] * length_of_nums
        prefix_product_array[0] = nums[0]
        suffix_product_array[length_of_nums - 1] = nums[length_of_nums - 1]

        for i in range(1, length_of_nums):
            prefix_product_array[i] = prefix_product_array[i - 1] * nums[i]
            suffix_product_array[length_of_nums - i - 1] = (
                suffix_product_array[length_of_nums - i] * nums[length_of_nums - i - 1]
            )

        result = []
        for i in range(length_of_nums):
            if i == 0:
                left_value = 1
            else:
                left_value = prefix_product_array[i - 1]
            if i == length_of_nums - 1:
                right_value = 1
            else:
                right_value = suffix_product_array[i + 1]
            result.append(left_value * right_value)
        return result


Solution().productExceptSelf([1, 2, 3, 4])
