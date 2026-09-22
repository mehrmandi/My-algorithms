import sys
import os

# --- LOCAL TESTING (Optional) ---
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")


def bishopLocation(n, m):
    for i in range(n):
        for j in range(m):
            if i == 0:
                print("A", end="")
            elif i == n - 1:
                print("B", end="")
            elif j == 0 and (i != 0 or i != n - 1):
                print("A", end="")
            elif j == m - 1 and (i != 0 or i != n - 1):
                print("B", end="")
            else:
                print(".", end="")
        print("")


def main():
    # Read all tokens at once
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))

    bishopLocation(n, m)


if __name__ == "__main__":
    main()
