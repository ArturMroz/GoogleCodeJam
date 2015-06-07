# Mushroom Monster
# https://code.google.com/codejam/contest/4224486/dashboard#s=p0

for tc in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    m1 = m2 = maxd = 0

    # calculating first method and getting max difference between plates
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            m1 += a[i] - a[i + 1]
            maxd = max(maxd, a[i] - a[i + 1])

    # calculating second method once max difference is known
    m2 = sum(min(maxd, x) for x in a[:-1])

    print('Case #{}: {} {}'.format(tc + 1, m1, m2))
