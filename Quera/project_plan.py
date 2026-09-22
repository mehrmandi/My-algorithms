import math


def solve():
    n = int(input())
    min_hour, max_hour = map(int, input().split())

    answer = math.ceil(n / max_hour)
    print(answer)


solve()




