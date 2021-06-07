s = "(1+(2*3)+((8)/4))+1"

def nested(s):
    max_depth = 0
    if s == "":
        return 0
    for i in range(len(s)):
        if s[i] != '(' or s[i] != ')':
            depth = s[:i].count('(')-s[:i].count(')')
            if depth>max_depth:
                max_depth=depth
    return max_depth

print(nested(s))