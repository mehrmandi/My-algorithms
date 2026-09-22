import sys
import os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")


def cafenetCap(c, g, it):
    comp = "0" * c
    for i in range(g):
        flag = True
        s = int(next(it))
        n = int(next(it))

        while flag and s + n <= len(comp) + 1:
            if comp[s - 1: s + n - 1] == "0" * n:
                comp = comp[0:s - 1] + "1" * n + comp[s - 1 + n:]
                flag = False
            else:
                s += 1
        print(comp)



def main():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    it = iter(input_data)

    x = int(next(it))
    y = int(next(it))

    cafenetCap(x, y, it)


if __name__ == "__main__":
    main()
