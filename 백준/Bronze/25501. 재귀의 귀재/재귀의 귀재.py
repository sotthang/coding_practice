def recursion(s, l, r):
    global c
    c += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def ispalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    s = input()
    c = 0
    print(ispalindrome(s), c)