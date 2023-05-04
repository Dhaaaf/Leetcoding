# Given a string s, find the length of the longest substring
#  without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        max_length = i = j = 0

        while i < n and j < n:
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1
                max_length = max(max_length, j - i)
            else:
                char_set.remove(s[i])
                i += 1

        return max_length
