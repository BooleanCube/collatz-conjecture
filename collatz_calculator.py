import math
import sys

delays = []


def measure_parameters(n):
    original = n
    odd = 0
    even = 0
    glide = 0
    mx = 0
    mn = 1e99
    residue = 1
    steps = [n]
    while n > 1:
        mn = min(mn, n)
        if n & 1:
            residue *= 1 + 1 / (3 * n)
            odd += 1
            even += 1
            n = (3 * n + 1)
            steps.append(n)
            mx = max(mx, n)
            n >>= 1
            steps.append(n)
        else:
            even += 1
            n >>= 1
            steps.append(n)
        if n < original and glide == 0:
            delay = odd + even
            glide = delay
    n = original
    delay = odd + even
    mn = 1 if mn == 2 else mn
    completeness = odd / even if n > 1 else None
    gamma = even / math.log(n, math.e) if n > 1 else None
    strength = 5 * odd - 3 * even
    level = -(strength / 8)
    shape = "Convergent" if mn == 1 else "Divergent" if mx < sys.maxsize else "Cyclic"
    return [delay, residue, glide, mx, mn, completeness, gamma, strength, level, shape, steps]


num = int(input("Input a number to measure parameters: "))
values = measure_parameters(num)

max_length = max(len(str(v))+1 for v in values[:-1])
print(max_length)
print("_"*(max_length+20) + "\n"
      "| Parameters     | Values" + " "*(max_length-7) + " |\n"
      "|----------------|-" + "-"*max_length + "|")
parameter_names = "Delay Residue Glide Maximum Minimum Completeness Gamma Strength Level Shape".split()
idx = 0
for param_string in parameter_names:
    value_string = str(values[idx])
    idx += 1
    print("| " + param_string + " "*(15-len(param_string)) + "| " + value_string + " "*(max_length-len(value_string)) + "|")
print("^" * (max_length + 20))

print("Steps: " + str(values[-1]))
