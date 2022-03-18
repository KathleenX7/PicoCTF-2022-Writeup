import os
import time

n = input()
s = time.time()
for i in range(100):
	os.system(f"echo {n} | ./pin_checker")
print(time.time() - s)