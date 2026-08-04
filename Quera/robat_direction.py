#  Number of commands
n = int(input())

#  commands
direction = input()

#  command equal number as anti-clockwise direction
turn_dict = {"R": 0, "D": 3, "L": 2, "U": 1}

#  define a function to convert commands to robat-format
def robatDir(dir, n):
    robat_dir = ""
    direction = 0
    i = 0
    while i < n:
        inter = turn_dict[dir[i]] - direction
        direction = turn_dict[dir[i]]
        i += 1
        if inter == 1 or inter == -3:
            robat_dir += "RF"
        elif inter == 2 or inter == -2:
            robat_dir += "RRF"
        elif inter == -1 or inter == 3:
            robat_dir += "RRRF"
        else:
            robat_dir += "F"
    print(robat_dir)





robatDir(direction, n)

