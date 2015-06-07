# Standing Ovation
# https://code.google.com/codejam/contest/6224486/dashboard#s=p0

for tc in range(int(input())):
    a = map(int, input().split()[1])
    t = ans = 0

    for i, x in enumerate(a):
        if x > 0 and i > t:
            d = i - t
            ans += d
            t += d
        t += x

    print('Case #{}: {}'.format(tc + 1, ans))
