import math
import random


# Calculates the line of best fit over a list of coordinates in the scatter plot
def best_fit_line(X, Y):
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    return b, a


def generate_coordinates(n):
    X = [0]
    Y = [math.log2(n)]
    c = 1
    while n > 1:
        if n % 2:
            n *= 3
            n += 1
        else:
            n >>= 1
        X.append(c)
        Y.append(math.log2(n))
        c += 1
    return X, Y


# number of samples tested
amount = 1000000
average_change = 0
slopes = []
for i in range(amount):
    n = random.randint(1, 10**32)
    X, Y = generate_coordinates(n)
    m, b = best_fit_line(X, Y)
    average_change += m
    slopes.append(m)

average_change /= amount
print(average_change)
