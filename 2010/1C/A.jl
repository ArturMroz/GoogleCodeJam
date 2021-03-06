# Rope Intranet
# https://code.google.com/codejam/contest/619102/dashboard#s=p0

for tc = 1:int(readline())
    n = int(readline())
    a = Vector{Int}[map(int, split(readline())) for _ = 1:n]
    ans = 0

    for (i, x) in enumerate(a)
        for y in a[i + 1:end]
            ans += (x[1] - y[1]) * (x[2] - y[2]) < 0
        end
    end

    println("Case #", tc, ": ", ans)
end