a, b, c, d, e, f = [int(x) for x in input().split(" ")]

def waterIce(a, b, d, e, f):
    box = [a, b]
    ice = [d, e, f]
    ice.sort()
    box.sort()
    
    if ice[0] <= box[0] and ice[1] <= box[1]:
        print("zende mimuni")
    else:
        print("dari mimiri")


# a, b, c, d, e, f = [4, 4, 100, 95, 3, 100]
waterIce(a, b, d, e, f)
