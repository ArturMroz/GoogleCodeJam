# All Your Base
# https://code.google.com/codejam/contest/189252/dashboard#s=p0

for tc in range(int(input())):
    s = input()
    v = 0
    d = {s[0]: 1}
    for j in s[1:]:
        if j not in d:
            d[j] = v
            v = v + 1 if v != 0 else 2

    b = max(v, 2)
    num = 0
    for i, c in enumerate(s):
        num += d[c] * b ** (len(s) - i - 1)

    print("Case #{}: {}".format(tc + 1, num))
