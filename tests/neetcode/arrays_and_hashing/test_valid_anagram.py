import pytest

from dsa.neetcode.arrays_and_hashing.valid_anagram import Solution

solution = Solution()


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "b", False),
        ("a", "a", True),
        ("aa", "a", False),
        ("a", "aa", False),
        ("ab", "ba", True),
        ("ab", "a", False),
        ("a", "ab", False),
    ],
)
def test_is_anagram(s, t, expected):
    assert solution.isAnagram(s, t) == expected
