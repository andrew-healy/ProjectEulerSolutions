def fibGen(n):
    first = 1
    yield first
    second = 2
    yield second
    while second <= n:
        second = first + second
        first = second - first
        yield second


n = 4000000
print('Computing using a generator')
fibSum = sum([i for i in fibGen(n) if i % 2 == 0])
print('The sum of the first {} even Fibonnaci numbers is {}'.format(n, fibSum))
