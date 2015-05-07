# Welcome to Code Jam
# https://code.google.com/codejam/contest/90101/dashboard#s=p2

p = "welcome to code jam"
for tc in range(int(input())):
    s = input()
    d = [0] * (len(p) + 1)
    d[0] = 1

    for c in s:
        for i in range(len(p)):
            if c == p[i]:
                d[i + 1] += d[i]

    print('Case #{}: {:04}'.format(tc + 1, d[-1] % 10000))
