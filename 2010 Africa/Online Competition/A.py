# Odd Man Out
# https://code.google.com/codejam/contest/438101/dashboard#s=p0&a=0

for tc in range(int(input())):
    n, g = input(), input().split()
    a = []
    for i in g:
        if i in a:
            a.remove(i)
        else:
            a.append(i)

    print("Case #{}: {}".format(tc + 1, a[0]))
