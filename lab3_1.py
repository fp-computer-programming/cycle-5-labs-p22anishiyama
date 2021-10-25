# Author: ATN 10/25/21

import time
import math

t1 = time.perf_counter()
math.pow(2, 2)

t2 = time.perf_counter()

speed1 = t2 - t1
print(speed1)

t3 = time.perf_counter()
2 ** 2

t4 = time.perf_counter()

speed2 = t4 - t3
print(speed2)
