class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> list[str]:
        start = 0
        end = 0
        result = []
        length = len(s)
        while end < length:
            if s[end] == "#":
                length_of_word = int(s[start:end])
                result.append(s[end + 1 : end + 1 + length_of_word])
                end += length_of_word + 1
                start = end
            else:
                end += 1
        return result
