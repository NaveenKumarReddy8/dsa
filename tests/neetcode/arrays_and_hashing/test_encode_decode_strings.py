import pytest

from dsa.neetcode.arrays_and_hashing.encode_decode_string import Solution

solution = Solution()


@pytest.mark.parametrize(
    "strs",
    [
        (["lint", "code", "love", "you"]),
        (["we", "say", ":", "yes"]),
        ([""]),
        ([]),
        (["", ""]),
        (["hello", "world"]),
        (["test with spaces"]),
    ],
)
def test_encode_decode(strs):
    encoded_string = solution.encode(strs)
    assert solution.decode(encoded_string) == strs
