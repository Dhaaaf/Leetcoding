# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.




# With Counter
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)

        if s1_len > s2_len:
            return False
        
        s1_counter = Counter(s1)
        window_counter = Counter()

        for i in range(s2_len):
            window_counter[s2[i]] += 1

            if i >= s1_len:
                window_counter[s2[i-s1_len]] -= 1
                if window_counter[s2[i-s1_len]] == 0:
                    del window_counter[s2[i-s1_len]]
            
            if s1_counter == window_counter:
                return True
        return False
    


# With Dictionaries
def checkInclusion(s1: str, s2: str) -> bool:
    s1_len, s2_len = len(s1), len(s2)
    if s1_len > s2_len:
        return False

    # Create dictionaries
    s1_dict = {ch: 0 for ch in s1}
    window_dict = {ch: 0 for ch in s1}

    for ch in s1:
        s1_dict[ch] += 1

    for i in range(s2_len):
        if s2[i] in window_dict:
            window_dict[s2[i]] += 1

        # Remove one character from the left side of the window
        if i >= s1_len and s2[i - s1_len] in window_dict:
            if window_dict[s2[i - s1_len]] == 1:
                del window_dict[s2[i - s1_len]]
            else:
                window_dict[s2[i - s1_len]] -= 1

        # Compare the frequency of characters in the current window with s1
        if s1_dict == window_dict:
            return True

    return False