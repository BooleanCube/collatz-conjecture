import time
import sys

dp = {1: 1}


def count_steps(n):
    steps = 0
    while n >= 1:
        if n in dp:
            return dp[n] + steps
        if n & 1:
            steps += 2
            n = (3 * n + 1) >> 1
        else:
            steps += 1
            n >>= 1
    return steps


start_time = time.time()

r = 10000000
for i in range(1, r + 1):
    steps = count_steps(i)
    dp[i] = steps

end_time = time.time()

sys.stdout.write(str(dp))
sys.stdout.write(f"\n\nTotal Execution Runtime: {end_time - start_time} sec")
