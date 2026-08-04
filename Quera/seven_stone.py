#  order of the stones
stone_order = [int(x) for x in input().split(" ")]

#  number of the stone that was struck
stone = int(input())

#  define a function to calculate the number of fallen stones
def stoneFall(order, s):
    i = 0
    for i in range(7):
        if order[i] == s:
            if i == 0:
                print(6)
            else:
                print(7 - i)
        i += 1


stoneFall(stone_order, stone)