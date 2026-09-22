import sys


def isAccess(d):
    if 0 in d and 1 in d:
        print("YES")
    else:
        print("NO")


def main():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    it = iter(input_data)

    n = int(next(it))
    m = int(next(it))

    d = [int(next(it)) for _ in range(n)]
    c = [int(next(it)) for _ in range(n)]

    isAccess(d)


if __name__ == "__main__":
    main()
