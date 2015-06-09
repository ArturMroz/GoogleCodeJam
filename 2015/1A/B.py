# Haircut
# https://code.google.com/codejam/contest/4224486/dashboard#s=p1


def solve(start, m):
    n = start
    c = [0] * len(m)

    while n > 0:
        # assign a customer for every idle barber
        while 0 in c:
            d = c.index(0)
            if n == 1:
                return d + 1
            c[d] = m[d]
            n -= 1

        # period has repeated, n can be reduced
        if all(x == 1 for x in c):
            period = start - n
            n = n % period or period

        # reduce time by 1 minute for all barbers
        for i in range(len(c)):
            c[i] -= 1

for tc in range(int(input())):
    b, n = (int(x) for x in input().split())
    m = [int(x) for x in input().split()]
    print('Case #{}: {}'.format(tc + 1, solve(n, m)))
