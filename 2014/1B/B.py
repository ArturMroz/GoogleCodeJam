# New Lottery Game
# https://code.google.com/codejam/contest/2994486/dashboard#s=p1

for tc in range(int(input())):
    a, b, k = map(int, input().split())
    
    if k > a or k > b: 
        ans = a * b
    else:
        ans = a * b - (a - k) * (b - k)
        for i in range(k, a):
        	for j in range(k, b):
        		ans += i & j < k

    print('Case #{}: {}'.format(tc + 1, ans))
