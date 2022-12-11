def locate_glide(n):
    start = n
    steps = 0
    while n > 1:
        if n & 1:
            n = (3 * n + 1) >> 1
            steps += 1
        else:
            n >>= 1
            steps += 1
        if n < start:
            return steps
    return steps


def generate_parity(n):
    steps = [n & 1]
    while n > 1:
        if n & 1:
            n = (3 * n + 1) >> 1
        else:
            n >>= 1
        steps.append(n & 1)
    return steps


n = int(input("Input a number to test the terras theorem: "))

print(f"Found finite stopping time: {locate_glide(n)}")
print(f"Parity Vector: {generate_parity(n)}")
