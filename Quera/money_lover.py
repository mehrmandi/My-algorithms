n = int(input())
coins = []
sum = 0
for i in range(n):
    h = int(input())
    coins.append(h)
    sum += h

def minMove(n, c, s):
    row = s // n
    move = 0

    for i in range(n):
        if coins[i] > row:
            ex = coins[i] - row
            move += ex

    print(move)


minMove(n, coins, sum)




