# Rope Intranet
# https://code.google.com/codejam/contest/619102/dashboard#s=p0

for tc in range(int(input())):
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i, x in enumerate(a):
        for y in a[i + 1:]:
            ans += (x[0] - y[0]) * (x[1] - y[1]) < 0

    print('Case #{}: {}'.format(tc + 1, ans))
