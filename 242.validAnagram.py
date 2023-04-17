# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return to_dict(s) == to_dict(t)

def to_dict(s):
    dict = {}

    for char in s:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
