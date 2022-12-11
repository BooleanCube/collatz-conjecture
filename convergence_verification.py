from io import StringIO
import sys
import time


class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def append(self, text):
        self._file_str.write(str(text))
        return self

    def to_string(self):
        return str(self)

    def __str__(self):
        return self._file_str.getvalue()


visited = {1: True}
threshold = pow(2, 8)
sieve = pow(2, 20)
sample = pow(2, 22)


def is_converging(n):
    steps = 0
    while n > 1:
        if steps > threshold:
            return False
        if n in visited:
            return visited[n]
        if n & 1:
            steps += 2
            n = (3 * n + 1) >> 1
        else:
            steps += 1
            n >>= 1
    return True


def count_steps(n):
    steps = 1
    while n > 1:
        if n & 1:
            steps += 2
            n = (3 * n + 1) >> 1
        else:
            steps += 1
            n >>= 1
    return steps


start_time = time.time()

output = StringBuilder()
for i in range(1, sample + sieve, sieve):
    non_converging = []
    for j in range(i, i + sieve):
        if j > sample:
            break
        m = j % 9
        if m == 2 or m == 4 or m == 5 or m == 8:
            visited[j] = True
            continue
        visited[j] = is_converging(j)
        if not visited[j]:
            non_converging.append(j)

    output.append(f"Sieve #{i // sieve}: \n")
    output.append(len(non_converging)).append("\n")
    for num in non_converging:
        output.append(f"D({num}) = {count_steps(num)}\n")
    output.append("-" * 20).append("\n")

end_time = time.time()

sys.stdout.write(str(output))
sys.stdout.write(f"\n\nTotal Execution Runtime: {end_time - start_time} sec")
