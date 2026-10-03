# Given a positive integer n, consider a 4n * 4n matrix filled with integers from 1 to(4n) * (4n) in row-major order(left to right, top to bottom). Form two coils from the matrix:

# The first coil starts from the top-left cell(0, 0) and spirals inward.
# The second coil starts from the bottom-right cell(4n - 1, 4n - 1) and spirals inward in the opposite direction.
# Return these two coils in the same order.

# Traverse Layer by Layer - O(n ^ 2) Time and O(n ^ 2) Space


def formCoils(n):
    m = 8 * n * n

    coil1 = [0] * m
    coil1[0] = 8 * n * n + 2 * n

    curr = coil1[0]
    flag = 1
    step = 2
    index = 1

    # Generate the standard first coil.
    while index < m:
        for _ in range(step):
            if index >= m:
                break
            curr -= 4 * n * flag
            coil1[index] = curr
            index += 1

        for _ in range(step):
            if index >= m:
                break
            curr += flag
            coil1[index] = curr
            index += 1

        flag *= -1
        step += 2

    # Generate the second coil using complementary values.
    coil2 = [16 * n * n + 1 - value for value in coil1]

    coil1.reverse()
    coil2.reverse()

    return [coil2, coil1]


if __name__ == "__main__":
    n = 1
    print(formCoils(n))


