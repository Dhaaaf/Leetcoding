# Given two strings, one is a subsequence if all of the elements of the first string occur in the same order within the second string. They do not have to be contiguous in the second string, but order must be maintained. For example, given the string 'I like cheese', the words('I', 'cheese') are one possible subsequence of that string. Words are space delimited.

# Given two string, s and t, where t is a subsequence of s, report the words of s, missing in t (case sensitive), in the order they are missing.

def missing_words(s, t):
    s_words = s.split()
    t_words = t.split()

    missing_words = []
    t_index = 0

    for s_word in s_words:
        if t_index < len(t_words) and s_word == t_words[t_index]:
            t_index += 1
        else:
            missing_words.append(s_word)

    return missing_words