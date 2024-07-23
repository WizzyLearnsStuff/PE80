from math import isqrt
sum(map(lambda p: sum(map(int, str(isqrt(p * (10 ** 200)))[:100])), filter(lambda k: (isqrt(k) ** 2) != k, range(1, 101))))
