from src.dsa.neetcode.arrays_and_hashing.encode_decode_string import Solution


def test_encode_decode_multiple_words():
    s = Solution()
    original_strs = ["hello", "world"]
    encoded_string = s.encode(original_strs)
    decoded_strs = s.decode(encoded_string)
    assert original_strs == decoded_strs


def test_encode_decode_long_word():
    s = Solution()
    original_strs = ["a" * 100]
    encoded_string = s.encode(original_strs)
    decoded_strs = s.decode(encoded_string)
    assert original_strs == decoded_strs


def test_encode_decode_multiple_long_words():
    s = Solution()
    original_strs = ["a" * 100, "b" * 50]
    encoded_string = s.encode(original_strs)
    decoded_strs = s.decode(encoded_string)
    assert original_strs == decoded_strs
