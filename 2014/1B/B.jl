# New Lottery Game
# https://code.google.com/codejam/contest/2994486/dashboard#s=p1

for tc in 1:int(readline())
    a::Int, b::Int, k::Int = map(int, split(readline()))
    # a, b, k = map(int, split(readline()))
    ans = 0

    for i in 0:a-1
    	for j in 0:b-1
    		ans += i & j < k
    	end
    end

	println("Case #", tc, ": ", ans)
end
