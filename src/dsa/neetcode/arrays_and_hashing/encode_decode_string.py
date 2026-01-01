class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> list[str]:
        start = 0
        end = 0
        length_of_s = len(s)
        result = []
        length_of_word = 0
        while start < length_of_s and end < length_of_s:
            if s[end] == "#":
                length_of_word = int(s[start:end])
                start = end + 1


print(Solution().encode(["leet", "code", "abcdefedfsadfsdsddsfsd"]))
