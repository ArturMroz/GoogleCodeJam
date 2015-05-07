# Snapper Chain
# https://code.google.com/codejam/contest/433101/dashboard#s=p0

for tc in range(int(input())):
    n, k = map(int, input().split())
    ans = all(k & 1 << i for i in range(n))
    print('Case #{}: {}'.format(tc + 1, 'ON' if ans else 'OFF'))
