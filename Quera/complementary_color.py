
t = int(input())

def complementaryColor():
    for i in range(t):
        s = input()
        s = s[1:]
        rgb = [s[i:i+2] for i in range(0, len(s), 2)]
        text = "#"
        for j in rgb:
            r = int(j, 16)
            com_col = 255 - r
            code = hex(com_col)[2:].zfill(2).upper()
            text += code
        print(text)




complementaryColor()
