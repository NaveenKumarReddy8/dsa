from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = defaultdict(list)
        for string in strs:
            anagram_groups["".join(sorted(string))].append(string)
        return list(anagram_groups.values())
