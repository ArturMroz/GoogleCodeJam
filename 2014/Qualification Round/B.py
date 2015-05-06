# Cookie Clicker Alpha
# https://code.google.com/codejam/contest/2974486/dashboard#s=p1


for tc in range(int(input())):
    c, f, x = map(float, input().split())
    s = 2.0
    t = 0.0

    while (x - c) / s > x / (s + f):
        t += c / s
        s += f

    t += x / s
    print('Case #{}: {:.7f}'.format(tc + 1, t))
