for tc in range(int(input())):
    a, b, k = map(int, input().split())
    ans = 0

    for i in range(a):
    	for j in range(b):
    		ans += i & j < k

    print('Case #{}: {}'.format(tc + 1, ans))
