import time
import random


while True:
    delta = time.time()
    while delta < delta+random.randint(100, 999):
        print('Hello World')