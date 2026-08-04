n = int(input())

def deltaMake (row):
    print((row - 1) * "." + "D" + (row - 1) * ".")
    new_row = row - 1
    i = 1
    while new_row - 1 > 0:
        print((new_row - 1) * "." + "D" + i * "." + "D" + (new_row - 1) * ".")
        new_row -= 1
        i += 2

    print((row - 1) * "D." + "D")


deltaMake(n)