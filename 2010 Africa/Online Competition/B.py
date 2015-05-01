# Get to Work
# https://code.google.com/codejam/contest/438101/dashboard#s=p1

for tc in range(int(input())):
    n, t = map(int, input().split())
    e = int(input())
    imp = False
    ans = [0] * n
    a = [tuple(map(int, input().split())) for i in range(e)]

    for i in range(n):
        if i + 1 == t:
            continue
        curr = [x for x in a if x[0] == i + 1]
        curr.sort(key=lambda x: x[1])
        while not imp and curr:
            ans[i] += 1
            driver = curr.pop()
            if not driver[1]:
                imp = True
            elif driver[1] > len(curr):
                break
            else:
                curr = curr[driver[1] - 1:]

    ans = "IMPOSSIBLE" if imp else ' '.join(map(str, ans))
    print("Case #{}: {}".format(tc + 1, ans))
