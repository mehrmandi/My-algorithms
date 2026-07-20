def removeZeroes(s):
    while len(s) > 1 and s[0] == "0":
        s = s[1:]
    return s


def makeNumeric(s):
    base = ord("0")
    i = len(s) - 1
    num = 0
    j = 0

    while i >= 0:
        eq = (ord(s[i]) - base) * (10**j)
        print("eq", eq)
        num += eq
        i -= 1
        j += 1

    return num


def multiplyString(s1, s2):
    flag = False

    first_s1 = s1[0]
    first_s2 = s2[0]

    if first_s1 == "-":
        s1 = s1[1:]
        if first_s2 != "-":
            flag = True
    if first_s2 == "-":
        s2 = s2[1:]
        if first_s1 != "-":
            flag = True

    s1 = removeZeroes(s1)
    s2 = removeZeroes(s2)

    num1 = makeNumeric(s1)
    num2 = makeNumeric(s2)

    if flag:
        return num1 * num2 * -1
    else:
        return num1 * num2


s1 = "-9"
s2 = "-2433"
print(multiplyString(s1, s2))
