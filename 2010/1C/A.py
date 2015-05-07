# Rope Intranet
# https://code.google.com/codejam/contest/619102/dashboard#s=p0

for tc in range(int(input())):
    a = [tuple(map(int, input().split())) for i in range(int(input()))]
    ans = 0
    for j in range(len(a)):
        for k in range(j + 1, len(a)):
            if a[j][0] > a[k][0] and a[j][1] < a[k][1] \
            or a[j][0] < a[k][0] and a[j][1] > a[k][1]:
                ans += 1

    print('Case #{}: {}'.format(tc + 1, ans))
