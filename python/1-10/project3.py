def largestPrimeFactor(n):
    j = n
    for i in xrange(2, n + 1):
        while j % i == 0:
            if j == i:
                return j
            j = j / i

print largestPrimeFactor(600851475143)