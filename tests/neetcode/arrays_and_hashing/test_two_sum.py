import pytest

from dsa.neetcode.arrays_and_hashing.two_sum import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ],
)
def test_two_sum(nums, target, expected):
    result = solution.twoSum(nums, target)
    assert result == expected
