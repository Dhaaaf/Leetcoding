# Write a function, token_transform, that takes in a dictionary of tokens and a string. In the dictionary, the replacement values for a token may reference other tokens. The function should return a new string where tokens are replaced with their fully evaluated string values.

# Tokens are enclosed in a pair of '$'.

# You may assume that there are no circular token dependencies.



def token_transform(s, tokens):
  output = ""
  i = 0
  j = 1
  while i < len(s):
    if s[i] != '$':
      output += s[i]
      i += 1
      j = i + 1
    elif s[j] != '$':
      j += 1
    else:
      key = s[i:j+1]
      value = tokens[key]
      evaluated_value = token_transform(value, tokens)
      tokens[key] = evaluated_value
      output += evaluated_value
      i = j + 1
      j = i + 1
  return output