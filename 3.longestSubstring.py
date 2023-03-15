# Given a string s, find the length of the longest substring
#  without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        j = 0
        char_set = set()
        for i in s:
            if i not in char_set:
                char_set.add(s)
                j += 1
            else:
                return j
