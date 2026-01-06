class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join([obj for obj in s.lower() if (obj != " " and obj.isalnum())])
        return result == result[::-1]
