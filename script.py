import time

t0 = time.time()
n = 0
while n < 1000000000:
    n += 1
t1 = time.time()

print(t1-t0)