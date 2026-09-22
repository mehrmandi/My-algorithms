import sys


def solve():
    # Use fast I/O for reading all integers at once
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    n = int(next(iterator))
    coins = []
    total_sum = 0

    for _ in range(n):
        val = int(next(iterator))
        coins.append(val)
        total_sum += val

    # Average value each pile should have
    target = total_sum // n

    moves = 0
    # Calculate the total excess of coins in piles greater than the target
    for coin in coins:
        if coin > target:
            moves += (coin - target)

    print(moves)


if __name__ == '__main__':
    solve()





