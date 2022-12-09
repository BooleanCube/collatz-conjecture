from matplotlib import pyplot as plt
import math

dp = {}

r = 10
digits = list(range(1, 10))
freq = [0]*len(digits)
for i in range(1, r + 1):
    n = i
    current = [0]*len(digits)
    while n > 1:
        if n in dp:
            for j in range(9):
                freq[j] += dp[n][j]
                current[j] += dp[n][j]
            break
        d = int(math.log10(n))
        fd = int(n / pow(10, d))
        freq[fd-1] += 1
        current[fd-1] += 1
        if n & 1:
            n = (3 * n + 1) // 2
        else:
            n >>= 1
    freq[0] += 1
    dp[i] = current

values = []
for a, f in zip(digits, freq):
    values.extend(a for _ in range(f))

fig, axs = plt.subplots(1, 1, figsize=(10, 6))

axs.hist(x=values, range=[1, 9], rwidth=0.9, align="mid", orientation="vertical")

plt.xlabel("First digit in steps count")
plt.ylabel("Frequency")
plt.title("Benford's Law")

plt.show()
