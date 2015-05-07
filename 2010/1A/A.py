# Rotate
# https://code.google.com/codejam/contest/544101/dashboard#s=p0


def check_h(c, k, B):
    for row in B:
        for i in range(len(row) - k + 1):
            if (row[i:i + k].count(c) == k):
                return True


def check_d(c, k, B):
    n = len(B)
    for i in range(n - k + 1):
        P = []
        P2 = []
        for j in range(n - 1 - i, -1, -1):
            P.append(B[j + i][n - j - 1])
            P2.append(B[n - j - 1 - i][j])

        for z in range(len(P)):
            if P[z:z + k].count(c) == k or P2[z:z + k].count(c) == k:
                return True


def check_d2(c, k, B):
    n = len(B)
    for i in range(n - k + 1):
        P = []
        P2 = []
        for j in range(n - i):
            P.append(B[j][j + i])
            P2.append(B[j + i][j])

        for z in range(len(P)):
            if P[z:z + k].count(c) == k or P2[z:z + k].count(c) == k:
                return True


def check_win(c, k, B):
    return check_h(c, k, B) or check_h(c, k, zip(*B)) \
        or check_d(c, k, B) or check_d2(c, k, B)


def get_winner(r, b):
    if r and b:
        return 'Both'
    elif not r and not b:
        return 'Neither'
    elif r:
        return 'Red'
    else:
        return 'Blue'


for tc in range(int(input())):
    n, k = map(int, input().split())
    B = [input().strip() for _ in range(n)]
    B2 = []
    for row in B:
        row2 = [c for c in row[::-1] if c != '.']
        row2 += ['.'] * (n - len(row2))
        B2.append(row2)

    r = check_win('R', k, B2)
    b = check_win('B', k, B2)
    print("Case #{}: {}".format(tc + 1, get_winner(r, b)))
