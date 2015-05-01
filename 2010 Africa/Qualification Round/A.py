# Store Credit
# https://code.google.com/codejam/contest/351101/dashboard#s=p0

for tc in range(int(input())):
    c, n = int(input()), int(input())
    p = [int(x) for x in input().split()]

    for x in range(n):
        if c - p[x] in p[x + 1:]:
            break

    ans = x + 1, x + 2 + p[x + 1:].index(c - p[x])
    print("Case #{}: {} {}".format(tc + 1, *ans))
