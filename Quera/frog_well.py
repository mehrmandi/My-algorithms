import sys


def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))

    results = []
    for _ in range(n):
        u = int(next(it))  
        d = int(next(it))  
        h = int(next(it))  

        if u >= h:
            results.append("1")
        else:
            net_gain = u - d
            days = 1 + (h - u + net_gain - 1) // net_gain
            results.append(str(days))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()



