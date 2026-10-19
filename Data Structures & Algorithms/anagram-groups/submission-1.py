from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}

        for string in strs:
            # Frequency of letters a-z
            count = [0] * 26

            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1

            # Lists cannot be dictionary keys, so convert to tuple
            signature = tuple(count)

            if signature in anagram_groups:
                anagram_groups[signature].append(string)
            else:
                anagram_groups[signature] = [string]

        return list(anagram_groups.values())