# number of friands
n = int(input())

#  The degree of intimacy of each friend
f_intim = [int(x) for x in input().split(" ")]


def maxIntimacy(array):
    max_intim = max(array)
    print('%.6f' % max_intim)


maxIntimacy(f_intim)