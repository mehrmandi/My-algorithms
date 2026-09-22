import sys


def solve():
    # Read all input values at once
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    missing_x = 0
    missing_y = 0
    missing_z = 0

    # In a rectangular cuboid (8 vertices), each coordinate component
    # appears an even number of times (4 times each).
    # Since one vertex is missing, the missing coordinate is the XOR sum
    # of the existing 7 coordinate values along each axis.
    for _ in range(7):
        x = int(next(iterator))
        y = int(next(iterator))
        z = int(next(iterator))

        missing_x ^= x
        missing_y ^= y
        missing_z ^= z

    # Output the coordinates of the missing vertex
    print(missing_x, missing_y, missing_z)


if __name__ == '__main__':
    solve()
