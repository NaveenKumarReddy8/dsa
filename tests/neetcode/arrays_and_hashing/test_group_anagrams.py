import pytest

from dsa.neetcode.arrays_and_hashing.group_anagrams import Solution

solution = Solution()


def sort_result(result: list[list[str]]) -> list[list[str]]:
    """Helper function to sort the result for comparison."""
    return sorted([sorted(group) for group in result])


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (
            ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"],
            [
                ["max"],
                ["buy"],
                ["doc"],
                ["may"],
                ["ill"],
                ["bar"],
                ["pew"],
                ["cab"],
                ["tin"],
                ["duh"],
            ],
        ),
        (["dddg", "gggd"], [["dddg"], ["gggd"]]),
        (["a", "b", "a"], [["a", "a"], ["b"]]),
    ],
)
def test_group_anagrams(strs, expected):
    """
    Tests the groupAnagrams function.
    The results are sorted before comparison because the order of anagram groups
    and the order of strings within a group does not matter.
    """
    actual = solution.groupAnagrams(strs)
    assert sort_result(actual) == sort_result(expected)
