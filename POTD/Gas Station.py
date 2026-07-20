# def checkCycle(gas, cost, start, index, res, n):
#     if res < 0:
#         return False
#
#     if index > n - 1:
#         index = 0
#
#     if index != start:
#         res += (gas[index] - cost[index])
#         return checkCycle(gas, cost, start, index + 1, res, n)
#
#     return True
#
#
#
#
# def gasStationCycle(gas, cost):
#     n = len(cost)
#
#     for i in range(n):
#         result = gas[i] - cost[i]
#         if result >= 0:
#             check = checkCycle(gas, cost, i, i + 1, result, n)
#             if check:
#                 return i
#
#     return -1


# --------------------------------------------------------------------

def startStation(gas, cost):
    n = len(gas)

    totalGas = 0
    currGas = 0
    startIdx = 0

    for i in range(n):
        currGas += gas[i] - cost[i]
        totalGas += gas[i] - cost[i]

        if currGas < 0:
            currGas = 0
            startIdx = i + 1

    if totalGas < 0:
        return -1

    return startIdx


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print(gasStationCycle(gas, cost))

# print(checkCycle([-2, -2, -2, 3, 3], 3, 4, 3, 5))
