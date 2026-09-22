import sys


def solve():
    data = sys.stdin.buffer.read().split()

    n = int(data[0])
    k = int(data[1])

    friends = [int(x) for x in data[2:2 + n]]
    friends.sort()

    taken = 0
    seats_left = k

    for f in friends:
        need = f + 1  
        if seats_left >= need:
            seats_left -= need
            taken += 1
        else:
            break

    print(taken)


if __name__ == "__main__":
    solve()







