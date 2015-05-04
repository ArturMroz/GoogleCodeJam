# Alien Language
# https://code.google.com/codejam/contest/90101/dashboard#s=p0

import re

l, d, n = map(int, input().split())
s = " ".join(input() for i in range(d))
for tc in range(n):
    p = input().replace('(', '[').replace(')', ']')
    r = len(re.findall(p, s))
    print('Case #{}: {}'.format(tc + 1, r))
