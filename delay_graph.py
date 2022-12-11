from matplotlib import pyplot as plt

dp = {1: 1}


def delay(n):
    original = n
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
    dp[original] = steps
    return steps


r = 10000
x = list(range(1, r+1))
y = []
for i in x:
    d = delay(i)
    y.append(d)

plt.scatter(x=x, y=y, s=500/r+0.15)
plt.show()
