



def findMissingDot():
    cube = []
    for i in range(7):
        cube_face = [int(x) for x in input().split(" ")]
        cube.append(cube_face)
    x = []
    y = []
    z = []
    for i in range(7):
        x.append(cube[i][0])
        y.append(cube[i][1])
        z.append(cube[i][2])
    x.sort()
    y.sort()
    z.sort()
    x1 = x.count(x[0])
    x2 = x.count(x[6])
    y1 = y.count(y[0])
    y2 = y.count(y[6])
    z1 = z.count(z[0])
    z2 = z.count(z[6])
    if x1 == 4:
        print(x[6], end=" ")
    else:
        print(x[0], end=" ")
    if y1 == 4:
        print(y[6], end=" ")
    else:
        print(y[0], end=" ")
    if z1 == 4:
        print(z[6], end=" ")
    else:
        print(z[0], end=" ")




findMissingDot()