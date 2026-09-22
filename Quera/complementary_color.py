def complementaryColor(t):
    for _ in range(t):
        s = input().strip()[1:]
        text = "#" + "".join(
            hex(255 - int(s[i:i+2], 16))[2:].zfill(2).upper()
            for i in range(0, len(s), 2)
        )
        print(text)


t = int(input())
complementaryColor(t)
