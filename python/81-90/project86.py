import math

N = 1000000

totalIntPaths = 0
M = 1

while totalIntPaths <= N:
    for P in xrange(2, 2 * M + 1):
        root = math.sqrt(P ** 2 + M ** 2)
        if root.is_integer():
            if P <= M:
                totalIntPaths += P / 2
            else:
                totalIntPaths += M - P / 2 + (P % 2 == 0)
        if totalIntPaths > N:
            break
    M += 1

print(M - 1)