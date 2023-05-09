# Write a function, detectDictionary, that takes in a dictionary of words and an alphabet string. The function should return a boolean indicating whether or not all words of the dictionary are lexically-ordered according to the alphabet.

# You can assume that all characters are lowercase a-z.

# You can assume that the alphabet contains all 26 letters.



def detect_dictionary(dictionary, alphabet):
  for i in range(0, len(dictionary) -1):
    current = dictionary[i]
    next = dictionary[i+1]
    if not lexical_order(current, next, alphabet):
      return False
  return True


def lexical_order(word_1, word_2, alphabet):
  length = max(len(word_1), len(word_2))
  for i in range(length):
    value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf')
    value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')  
    if value_1 < value_2:
      return True
    elif value_2 < value_1:
      return False
  return True