s = "abcdefg"
k = 2

i = 0
p = list(s)
while i < len(s):
    m = p[i:i + k]
    print(m)
    m = m[::-1]
    print(m)
    p[i:i + k] = m
    i += 2 * k
    print(i)
print("".join(p))