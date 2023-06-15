# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.





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