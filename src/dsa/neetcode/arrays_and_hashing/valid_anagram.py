class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Pythonic
        # Time Complexity: O(nlogn) Due to the sorting
        # Space Complexity: O(n)
        # return sorted(s) == sorted(t)

        # Pythonic method 2:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # return Counter(s) == Counter(t)

        # Generic
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

        for char in t:
            if char not in counter:
                return False
            else:
                counter[char] -= 1
                if counter[char] < 0:
                    return False
        return True
