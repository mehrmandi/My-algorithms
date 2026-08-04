import math

#  q is the number of questions
#  t is Peygir answer interval
q, t = [int(x) for x in input().split(" ")]


#  define a function to calculate the name of ith chat author
def personName(number, interval):
    i = 0
    for i in range(number):
        chat_num = int(input())
        n = math.ceil(chat_num / (interval + 1))
        other_num = (chat_num - n) % 3
        if chat_num % (interval + 1) == 1:
            print("Peygir")
        elif other_num == 1:
            print("Tannaz")
        elif other_num == 2:
            print("Jeddy")
        else:
            print("Morshed")
        i += 1



personName(q, t)