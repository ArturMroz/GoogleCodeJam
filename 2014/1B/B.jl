# New Lottery Game
# https://code.google.com/codejam/contest/2994486/dashboard#s=p1

for tc in 1:int(readline())
    a::Int, b::Int, k::Int = (map(int, split(readline())))
    
    if k > a || k > b 
        ans = a * b
    else
        ans = a * b - (a - k) * (b - k)
        for i in k:a-1
            for j in k:b-1
                ans += i & j < k
            end
        end
    end 

	println("Case #", tc, ": ", ans)
end
