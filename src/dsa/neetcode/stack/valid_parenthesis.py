class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        char_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        for char in s:
            if char in char_map:
                stack.append(char)
            else:
                if (not stack) or (char_map[stack.pop()] != char):
                    return False
        return not stack
