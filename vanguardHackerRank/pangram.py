# A string is a pangram if it contains every letter [a-z].  Given a list of strings determine if each one is a pangram or not. "1" if true and "0" if not

def isPangram(pangram):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
    pangram_detection_results = ""

    for string in pangram:
        string_set = set(string.lower())

        if alphabet.issubset(string_set):
            pangram_detection_results += "1"
        else:
            pangram_detection_results += "0"

    return pangram_detection_results