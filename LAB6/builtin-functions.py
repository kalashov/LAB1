# 1
from functools import reduce

a = [2, 3, 4, 5]
p = reduce(lambda x, y: x * y, a)
print(p)

# 2
def f(s):
    upr = sum(1 for c in s if c.isupper())
    lwr = sum(1 for c in s if c.islower())
    return upr, lwr

s = input()
up_cnt, low_cnt = f(s)
print(up_cnt, low_cnt)

# 3
def is_pal(s):
    return s == s[::-1]

s = input()
print(is_pal(s))

# 4
import time
import math

n = int(input())
ms = int(input())

time.sleep(ms / 1000)
res = math.sqrt(n)
print(f"Square root of {n} after {ms} milliseconds is {res}")

# 5
tuplic = (True, True, True, False)

res = all(tuplic)
print(res)