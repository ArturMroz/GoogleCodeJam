# Multi-base happiness
# https://code.google.com/codejam/contest/188266/dashboard#s=p0


def ishappy(x, base, curr=[]):
    global sad, happy
    curr = curr or []

    if x in happy[base]:
        happy[base].update(curr)
        return True
    if x in curr or x in sad[base]:
        sad[base].update(curr)
        return False

    curr.append(x)
    s = 0
    while x:
        s += (x % base) ** 2
        x //= base

    return ishappy(s, base, curr)

# cache for sad and happy numbers in all bases
sad = [set() for i in range(11)]
happy = [{1} for i in range(11)]

for tc in range(int(input())):
    bases = list(map(int, input().split()))
    if 2 in bases:
        bases.remove(2)  # all numbers in base 2 are happy \o/
    i = 2
    while True:
        r = True
        for b in bases:
            r &= ishappy(i, b)
            if not r:
                break
        if r:
            print('Case #{}: {}'.format(tc + 1, i))
            break
        i += 1
