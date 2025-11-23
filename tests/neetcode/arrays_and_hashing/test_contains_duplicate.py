import pytest

from dsa.neetcode.arrays_and_hashing.contains_duplicate import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([], False),
        ([1], False),
        ([1, 1, 1, 1], True),
    ],
)
def test_has_duplicate(nums, expected):
    assert solution.hasDuplicate(nums) == expected
