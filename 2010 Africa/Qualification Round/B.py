# Reverse Words
# https://code.google.com/codejam/contest/351101/dashboard#s=p1

for tc in range(int(input())):
    ans = " ".join(input().split()[::-1])
    print("Case #{}: {}".format(tc + 1, ans))
