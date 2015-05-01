# Reverse Words
# https://code.google.com/codejam/contest/351101/dashboard#s=p1

for i in range(int(input())):
    r = " ".join(input().split()[::-1])
    print("Case #{}: {}".format(i + 1, r))
