# Consider a string consisting of the characters < and > only. The string is balanced if each < always appears before a corresponding > character (they do not need to be adjacent). Moreover, each < and > act as a unique pair of symbols and neither symbol can be considered as part of any other pair of symbols.

# To balance a string, any > character can be replaced with < >. Given an expression and a maximum number of replacements, determine whether the string can be balanced.

# expressions = ['<<>>', '<>', '<><>', '>>', '<<>', '><><']
# MaxReplacements = [0,1,2,2,2,2]
# Each of the first three are balanced already. The next one can be balanced in 2 moves, and neither of the last 2 can be balanced.

def balance_strings(expressions, max_replacements):
    result = []
    for exp, max_rep in zip(expressions, max_replacements):
        balance = 0
        replacements = 0
        for char in exp:
            if char == '<':
                balance += 1
            elif char == '>':
                if balance > 0:
                    balance -= 1
                elif replacements < max_rep:
                    replacements += 1
                else:
                    result.append(False)
                    break
        else:
            result.append(balance == 0)
    return result
