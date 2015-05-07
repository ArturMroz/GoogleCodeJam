# The Next Number
# https://code.google.com/codejam/contest/186264/dashboard#s=p1


def next_permutation(s):
    for i in range(len(s) - 1, 0, -1):
        if s[i] > s[i - 1]:
            for j in range(len(s) - 1, i - 1, -1):
                if s[j] > s[i - 1]:
                    t = list(s)
                    t[i - 1], t[j] = t[j], t[i - 1]
                    t[i:] = t[i:][::-1]
                    return ''.join(t), True
    return s[::-1], False

for tc in range(int(input())):
    num, res = next_permutation(input())
    if not res:
        a = list(num)
        i = next(j for j, x in enumerate(a) if x != '0')
        a[i], a[0] = a[0], a[i]
        a.insert(1, '0')
        num = ''.join(a)
    print('Case #{}: {}'.format(tc + 1, num))
