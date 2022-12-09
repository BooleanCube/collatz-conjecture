dp = {}


def countSteps(n):
    steps = 0
    while n > 1:
        if n in dp:
            return dp[n] + steps
        if n % 2:
            steps += 2
            n = (3 * n + 1) // 2
        else:
            steps += 1
            n >>= 1
    return steps


r = 1000000
for i in range(1, r + 1):
    steps = countSteps(i)
    dp[i] = steps

print(dp)
