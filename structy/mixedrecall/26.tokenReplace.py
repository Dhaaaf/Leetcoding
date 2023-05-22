# Write a function, token_replace, that takes in a dictionary of tokens and a string. The function should return a new string where tokens are replaced.

# Tokens are enclosed in a pair of '$'. You can assume that the input string is properly formatted. Tokens should be replaced from left to right in the string (see test_05).


def token_replace(s, tokens):
  output = ""
  i = 0
  j = 1
  while i < len(s):
    if s[i] != '$':
      output += s[i]
      i += 1
      j = i + 1
    elif s[j] != '$':
      j+=1
    else:
      key = s[i:j+1]
      output += tokens[key]
      i = j + 1
      j = i + 1
  return output