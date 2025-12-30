# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result


solution = Solution()

encoded_str = solution.encode(["lint", "code", "love", "you"])
print(encoded_str)

decoded_str = solution.decode(encoded_str)
print(decoded_str)
