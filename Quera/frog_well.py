#  number of input try
n = int(input())

#  Define a function to calculate the departure day
def dayCount(array):
    try_day = 0
    height = 0
    while height < array[2]:
        try_day += 1
        height += array[0]
        if height < array[2]:
            height -= array[1]
    print(try_day)

#  Get properties inputs n times
for i in range(n):
    try_prop = [int(x) for x in (input().split(" "))]
    dayCount(try_prop)




