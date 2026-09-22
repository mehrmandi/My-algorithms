
import sys


def solve():
    # Read all tokens from standard input
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    # Read the number of friends
    n = int(next(iterator))

    # Read the intimacy values
    intimacies = [int(next(iterator)) for _ in range(n)]

    # Find the maximum intimacy value
    max_val = max(intimacies)

    # Format output to 6 decimal places using modern f-string formatting
    sys.stdout.write(f"{max_val:.6f}\n")


if __name__ == '__main__':
    solve()
