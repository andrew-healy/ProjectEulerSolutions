lastDigitPairs = [(7, 7), (3, 3), (9, 1)]


def isPal(num):
    numStr = str(num)
    return numStr == numStr[::-1]

pals = []

for i in xrange(10):
    for j in xrange(10):
        for last in lastDigitPairs:
            m = int('9{}{}'.format(i, last[0]))
            n = int('9{}{}'.format(j, last[1]))
            prod = m * n
            if isPal(prod):
                pals.append(prod)

print(sorted(pals)[-1])