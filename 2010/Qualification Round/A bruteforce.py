# Snapper Chain
# https://code.google.com/codejam/contest/433101/dashboard#s=p0

for tc in range(int(input())):
    n, k = map(int, input().split())
    s = [False] * n
    for snap in range(k):
        for m in range(len(s) - 1, 0, -1):
            if all(s[:m]):
                s[m] = not s[m]
        s[0] = not s[0]

    print('Case #{}: {}'.format(tc + 1, 'ON' if all(s) else 'OFF'))
