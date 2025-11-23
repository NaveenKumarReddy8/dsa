import pytest

from dsa.neetcode.arrays_and_hashing.top_k_frequent_elements import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([-1, -1], 1, [-1]),
    ],
)
def test_top_k_frequent(nums, k, expected):
    """
    Tests the topKFrequent function.
    The results are sorted before comparison because the order of the top k elements
    does not matter.
    """
    result = solution.topKFrequent(nums, k)
    assert sorted(result) == sorted(expected)
