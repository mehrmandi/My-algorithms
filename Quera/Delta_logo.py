import sys


def deltaMake(row):
    # Base case for height 1
    if row == 1:
        print("D")
        return

    # Top vertex
    print("." * (row - 1) + "D" + "." * (row - 1))

    # Middle hollow rows
    for k in range(1, row - 1):
        outer_dots = "." * (row - 1 - k)
        inner_dots = "." * (2 * k - 1)
        print(outer_dots + "D" + inner_dots + "D" + outer_dots)

    # Bottom row alternating D and .
    print("D." * (row - 1) + "D")


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    deltaMake(n)


if __name__ == "__main__":
    main()
