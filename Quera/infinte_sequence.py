import sys


def solve():
    # Use fast I/O to read all inputs at once
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    # Read the number of test cases
    n = int(next(iterator))

    results = []

    for _ in range(n):
        seq = int(next(iterator))

        # Apply the logic logic based on the sequence rules
        if seq == 1:
            results.append("2")
        else:
            res = (seq - 1) % 4
            if res == 1:
                results.append("1")
            elif res == 2:
                results.append("-3")
            elif res == 3:
                results.append("2")
            else:  # res == 0
                results.append("-2")

    # Print all results at once for maximum performance
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == '__main__':
    solve()
