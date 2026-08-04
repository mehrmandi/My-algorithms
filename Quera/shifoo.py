t = int(input())

def combWord(w):
    sum = 0
    i = 1
    while i < len(w):
        for j in range(i):
            if w[i][-1:] == w[j][0:1]:
                comb = str(w[i] + w[j][1:])
                w[j] = comb
                w.remove(w[i])
                i -= 1
            elif w[i][0:1] == w[j][-1:]:
                comb = str(w[j] + w[i][1:])
                w[i] = comb
                w.remove(w[j])
                i -= 1
        i += 1
    for item in w:
        sum += len(item)

    return sum


def lenword():
    s = int(input())
    word = []
    for j in range(s):
        w = input()
        word.append(w)

    wr = list(reversed(word))

    minlen = min(combWord(word), combWord(wr))

    return minlen



for i in range(t):
    print(lenword())




