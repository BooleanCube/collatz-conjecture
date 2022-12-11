from matplotlib import pyplot as plt


def glide(n):
    start = n
    steps = 0
    while n > 1:
        if n & 1:
            n = (3 * n + 1) >> 1
            steps += 2
        else:
            n >>= 1
            steps += 1
        if n < start:
            return steps
    return steps


r = 10000
x = list(range(2, r+1))
y = []
for i in x:
    d = glide(i)
    y.append(d)

plt.scatter(x=x, y=y, s=500/r+0.15)
plt.show()
