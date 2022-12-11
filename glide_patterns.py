import heapq
import math


def dropping_time(n):
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


r = 1000000

pattern = [1]
for i in range(3, r+1, 2):
    d = dropping_time(i)
    pattern.append(d)
pattern = sorted(set(pattern))

indices = list(range(1, len(pattern)+1))

diff = ["-"]
for i in range(1, len(pattern)):
    diff.append(pattern[i]-pattern[i-1])

print("_____________________________________\n"
      "| Index     | Glides        | Delta |\n"
      "|-----------|---------------|-------|")
for i in range(len(indices)):
    index_string = str(indices[i])
    lis = len(index_string)
    pattern_string = str(pattern[i])
    lps = len(pattern_string)
    diff_string = str(diff[i])
    lds = len(diff_string)
    print("| " + index_string + " "*(10-lis) + "| " + pattern_string + " "*(14-lps) + "| " + diff_string + " "*(6-lds) + "|")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

