
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # variable longest prefix 
        # set this to strs[i]
        # iterate through and compare longest prefix to next string
        # shorten our prefix, or return false

        prefix = strs[0]
        length = len(prefix)
        length_list = len(strs)
        if len(prefix) == 0:
            return ""

        for string in strs:
            # compare and subtract mostly
            while length > 0 and prefix[0:length] != string[0:length]:
                length = length -1
                if length == 0:
                    return ""
        return prefix[0:length]
