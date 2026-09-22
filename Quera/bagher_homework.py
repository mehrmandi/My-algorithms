import sys
import os

# Local testing: reads from input.txt if present
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")


def is_triangle(a: int, b: int, c: int) -> None:
    # Check if angles form a valid non-degenerate triangle
    if a + b + c != 180 or a <= 0 or b <= 0 or c <= 0:
        sys.stdout.write("No\n")
    else:
        sys.stdout.write("Yes\n")


def main():
    # Read all tokens directly
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    a = int(next(it))
    b = int(next(it))
    c = int(next(it))

    is_triangle(a, b, c)


if __name__ == "__main__":
    main()
