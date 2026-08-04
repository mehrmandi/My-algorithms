#  number of question
n = int(input())

#  define a function to show the i th number of sequence
#  we have a repeating sequence of 1 -3 2 -2
def seqCalc(n):
    for i in range(n):
        seq = int(input())
        res = (seq - 1) % 4
        if seq == 1:
            print(2)
        elif res == 1:
            print(1)
        elif res == 2:
            print(-3)
        elif res == 3:
            print(2)
        else:
            print(-2)

seqCalc(n)