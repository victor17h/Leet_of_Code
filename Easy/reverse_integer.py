x = -123


def reverse(x):
    if x > 2**31-1 or x < -2**31:
        return 0
    else:
        strg = str(x)
        if x > 0:
            rev = strg[::-1]
        else:
            temp = strg[1:]
            temp2 = temp[::-1]
            rev = "-" + temp2
        if int(rev) > 2**31-1 or int(rev) < -2**31:
            return 0
        else:
            return int(rev)

print(reverse(x))

