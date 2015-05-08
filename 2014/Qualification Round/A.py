# Magic Trick
# https://code.google.com/codejam/contest/2974486/dashboard#s=p0

for tc in range(int(input())):
    r1, a1 = int(input()) - 1, [input().split() for _ in range(4)]
    r2, a2 = int(input()) - 1, [input().split() for _ in range(4)]
    a = [x for x in a1[r1] if x in a2[r2]]

    if not a:
        ans = 'Volunteer cheated!'
    elif len(a) == 1:
        ans = a[0]
    else:
        ans = 'Bad magician!'

    print('Case #{}: {}'.format(tc + 1, ans))
